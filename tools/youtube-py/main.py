import re

from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    """YouTube URL에서 video ID를 추출합니다."""
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    if video_id_match:
        return video_id_match.group(1)
    return None


def get_transcript(url):
    """YouTube 동영상의 자막을 가져옵니다."""
    video_id = extract_video_id(url)
    if not video_id:
        print("유효한 YouTube URL이 아닙니다.")
        return None

    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["ko", "en"])
        return transcript_list
    except Exception as e:
        print(f"자막을 가져오는 중 오류가 발생했습니다: {e}")
        return None


def main():
    url = "https://www.youtube.com/watch?v=7ji0jHcdq1A"
    transcript = get_transcript(url)

    if transcript:
        print(f"YouTube 영상 '{url}'의 자막:")
        for entry in transcript:
            print(f"[{entry['start']:.2f}s]: {entry['text']}")

        # 자막 전체 텍스트를 하나의 문자열로 만들기
        full_text = " ".join([entry["text"] for entry in transcript])
        print("\n전체 자막 텍스트:")
        print(full_text)


if __name__ == "__main__":
    main()
