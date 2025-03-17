import { YoutubeLoader } from '@langchain/community/document_loaders/web/youtube';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

/**
 * YouTube 동영상의 자막과 메타데이터를 추출하고 파일로 저장하는 클래스
 */
class YouTubeTranscriptSaver {
  /**
   * YouTube URL로부터 자막과 메타데이터를 추출합니다.
   * @param {string} url - YouTube 동영상 URL
   * @param {Object} options - 옵션 객체
   * @param {string} options.language - 자막 언어 (기본값: 'en')
   * @param {boolean} options.addVideoInfo - 동영상 정보 추가 여부 (기본값: true)
   * @returns {Promise<Array>} 추출된 문서 객체 배열
   */
  static async extractTranscript(
    url,
    options = { language: 'en', addVideoInfo: true },
  ) {
    try {
      const loader = YoutubeLoader.createFromUrl(url, options);
      const docs = await loader.load();
      return docs;
    } catch (error) {
      console.error('자막 추출 중 오류가 발생했습니다:', error.message);
      throw error;
    }
  }

  /**
   * 추출한 문서를 다양한 형식으로 저장합니다.
   * @param {Array} docs - 문서 객체 배열
   * @param {Object} options - 저장 옵션
   * @param {string} options.outputDir - 출력 디렉토리 (기본값: 'output')
   * @param {boolean} options.saveText - 텍스트 파일로 저장 여부 (기본값: true)
   * @param {boolean} options.saveJson - JSON 파일로 저장 여부 (기본값: true)
   * @param {boolean} options.saveMarkdown - Markdown 파일로 저장 여부 (기본값: false)
   */
  static async saveToFiles(
    docs,
    options = {
      outputDir: 'output',
      saveText: true,
      saveJson: true,
      saveMarkdown: false,
    },
  ) {
    if (!docs || !docs.length) {
      console.error('저장할 문서가 없습니다.');
      return;
    }

    const doc = docs[0]; // 현재는 첫 번째 문서만 처리
    const { source, title } = doc.metadata;

    // 파일명 생성 (특수문자 제거 및 공백을 언더스코어로 대체)
    const safeTitle = title
      ? title.replace(/[^\w\s]/gi, '').replace(/\s+/g, '_')
      : source;

    // 출력 디렉토리 생성
    const outputDir = options.outputDir;
    await fs.mkdir(outputDir, { recursive: true });

    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    const baseFilename = `${safeTitle}_${timestamp}`;

    const tasks = [];

    // 텍스트 파일로 저장
    if (options.saveText) {
      const textContent =
        `제목: ${doc.metadata.title || '제목 없음'}\n` +
        `설명: ${doc.metadata.description || '설명 없음'}\n` +
        `작성자: ${doc.metadata.author || '작성자 정보 없음'}\n` +
        `조회수: ${doc.metadata.view_count || '조회수 정보 없음'}\n` +
        `URL: https://youtu.be/${source}\n\n` +
        `--- 자막 텍스트 ---\n\n` +
        `${doc.pageContent}`;

      tasks.push(
        fs
          .writeFile(
            path.join(outputDir, `${baseFilename}.txt`),
            textContent,
            'utf8',
          )
          .then(() =>
            console.log(`텍스트 파일이 저장되었습니다: ${baseFilename}.txt`),
          ),
      );
    }

    // JSON 파일로 저장
    if (options.saveJson) {
      const jsonContent = JSON.stringify(doc, null, 2);
      tasks.push(
        fs
          .writeFile(
            path.join(outputDir, `${baseFilename}.json`),
            jsonContent,
            'utf8',
          )
          .then(() =>
            console.log(`JSON 파일이 저장되었습니다: ${baseFilename}.json`),
          ),
      );
    }

    // Markdown 파일로 저장
    if (options.saveMarkdown) {
      const markdownContent =
        `# ${doc.metadata.title || '제목 없음'}\n\n` +
        `- **URL**: [https://youtu.be/${source}](https://youtu.be/${source})\n` +
        `- **작성자**: ${doc.metadata.author || '작성자 정보 없음'}\n` +
        `- **조회수**: ${doc.metadata.view_count || '조회수 정보 없음'}\n\n` +
        `## 설명\n\n${doc.metadata.description || '설명 없음'}\n\n` +
        `## 자막 텍스트\n\n\`\`\`\n${doc.pageContent}\n\`\`\``;

      tasks.push(
        fs
          .writeFile(
            path.join(outputDir, `${baseFilename}.md`),
            markdownContent,
            'utf8',
          )
          .then(() =>
            console.log(`Markdown 파일이 저장되었습니다: ${baseFilename}.md`),
          ),
      );
    }

    await Promise.all(tasks);
    return baseFilename;
  }
}

/**
 * 메인 함수 - 프로그램의 진입점
 */
async function main() {
  try {
    // 명령행 인수 파싱
    const args = process.argv.slice(2);
    const url = args[0] || 'https://youtu.be/bZQun8Y4L2A'; // 기본 URL
    const language = args[1] || 'ko';

    console.log(
      `YouTube URL(${url})에서 ${language} 언어의 자막을 추출합니다...`,
    );

    const docs = await YouTubeTranscriptSaver.extractTranscript(url, {
      language: language,
      addVideoInfo: true,
    });

    console.log('자막을 성공적으로 추출했습니다.');

    // 현재 스크립트 위치 기준으로 output 폴더 생성
    const __dirname = path.dirname(fileURLToPath(import.meta.url));
    const outputDir = path.join(__dirname, 'output');

    await YouTubeTranscriptSaver.saveToFiles(docs, {
      outputDir: outputDir,
      saveText: false,
      saveJson: false,
      saveMarkdown: true,
    });

    console.log(`모든 파일이 ${outputDir} 폴더에 성공적으로 저장되었습니다.`);
  } catch (error) {
    console.error('오류가 발생했습니다:', error);
    process.exit(1);
  }
}

async function customMain() {
  const urls = [
    'https://www.youtube.com/watch?v=IHMHVoH24eQ',
    'https://www.youtube.com/watch?v=CqcuQ0MxqWo',
    'https://www.youtube.com/watch?v=oj1vtV9XvD0',
    'https://www.youtube.com/watch?v=lr6wyxsFtk0',
    'https://www.youtube.com/watch?v=znKSUzbH6tk',
    'https://www.youtube.com/watch?v=5uYx5HyCNZ8',
    'https://www.youtube.com/watch?v=B9a3Abtp-JQ',
    'https://www.youtube.com/watch?v=HG_Vgt8fc4A',
    'https://www.youtube.com/watch?v=tQuQPmnoQTg',
    'https://www.youtube.com/watch?v=BdhSI-qiW8s',
    'https://www.youtube.com/watch?v=O1oWju5JRFM',
    'https://www.youtube.com/watch?v=VxlBE6hM8ic',
    'https://www.youtube.com/watch?v=IVuc6xS9kZk',
    'https://www.youtube.com/watch?v=qGkgRekEHbg',
    'https://www.youtube.com/watch?v=nL2qMD9UTBg',
    'https://www.youtube.com/watch?v=n4UdMXxBoWg',
    'https://www.youtube.com/watch?v=NM2SQKP63I4',
    'https://www.youtube.com/watch?v=MlTE3GipXl4',
    'https://www.youtube.com/watch?v=ymbkw_5gkwE',
    'https://www.youtube.com/watch?v=5wSfvYFdlH8',
  ];
  try {
    for (const url of urls) {
      // 명령행 인수 파싱
      const language = 'ko';

      console.log(
        `YouTube URL(${url})에서 ${language} 언어의 자막을 추출합니다...`,
      );

      const docs = await YouTubeTranscriptSaver.extractTranscript(url, {
        language: language,
        addVideoInfo: true,
      });

      console.log('자막을 성공적으로 추출했습니다.');

      // 현재 스크립트 위치 기준으로 output 폴더 생성
      const __dirname = path.dirname(fileURLToPath(import.meta.url));
      const outputDir = path.join(__dirname, 'output');

      await YouTubeTranscriptSaver.saveToFiles(docs, {
        outputDir: outputDir,
        saveText: false,
        saveJson: false,
        saveMarkdown: true,
      });

      console.log(`모든 파일이 ${outputDir} 폴더에 성공적으로 저장되었습니다.`);
    }
  } catch (error) {
    console.error('오류가 발생했습니다:', error);
    process.exit(1);
  }
}

// 스크립트가 직접 실행된 경우에만 main 함수 호출
if (import.meta.url === `file://${process.argv[1]}`) {
  // main();
  customMain();
}

export { YouTubeTranscriptSaver };
