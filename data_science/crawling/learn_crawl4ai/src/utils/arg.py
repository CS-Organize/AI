import argparse
import sys
from typing import List, Optional

from crawl4ai import CacheMode


def setup_argparse():
    """
    명령줄 인수 파서를 설정합니다.

    Returns:
        argparse.ArgumentParser: 설정된 인수 파서
    """
    parser = argparse.ArgumentParser(description="웹 크롤링 유틸리티")

    # 필수 인수
    parser.add_argument("url", nargs="?", help="크롤링할 URL (없을 경우 --url-list 사용)")

    # 브라우저 설정
    browser_group = parser.add_argument_group("브라우저 설정")
    browser_group.add_argument(
        "--browser",
        choices=["chromium", "firefox", "webkit"],
        default="chromium",
        help="사용할 브라우저 (기본값: chromium)",
    )
    browser_group.add_argument(
        "--headless",
        action="store_true",
        default=False,
        help="헤드리스 모드 실행 여부 (기본값: False)",
    )
    browser_group.add_argument(
        "--user-agent",
        help="사용자 에이전트 문자열",
    )
    browser_group.add_argument(
        "--mobile",
        action="store_true",
        default=False,
        help="모바일 브라우저 모드 (기본값: False)",
    )
    browser_group.add_argument(
        "--disable-security",
        action="store_true",
        default=False,
        help="웹 보안 비활성화 (기본값: False)",
    )

    # 크롤러 설정
    crawler_group = parser.add_argument_group("크롤러 설정")
    crawler_group.add_argument(
        "--cache-mode",
        choices=[cm.value for cm in CacheMode],
        default=CacheMode.ENABLED.value,
        help="캐시 모드 (기본값: ENABLED)",
    )
    crawler_group.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        default=False,
        help="상세 로깅 활성화 (기본값: False)",
    )
    crawler_group.add_argument(
        "--stream",
        action="store_true",
        default=False,
        help="스트리밍 모드 활성화 (기본값: False)",
    )
    crawler_group.add_argument(
        "--session-id",
        help="세션 ID (상태 유지를 위한 식별자)",
    )
    crawler_group.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="타임아웃 (초) (기본값: 30)",
    )
    crawler_group.add_argument(
        "--css-selector",
        help="컨텐츠 선택을 위한 CSS 선택자",
    )
    crawler_group.add_argument(
        "--js-code",
        help="페이지에서 실행할 JavaScript 코드",
    )

    # URL 관련 설정
    url_group = parser.add_argument_group("URL 설정")
    url_group.add_argument(
        "--url-list",
        help="URL 목록 파일 경로 (한 줄에 하나의 URL)",
    )
    url_group.add_argument(
        "--max-urls",
        type=int,
        default=0,
        help="크롤링할 최대 URL 수 (0: 무제한) (기본값: 0)",
    )

    # 딥 크롤링 설정
    deep_group = parser.add_argument_group("딥 크롤링 설정")
    deep_group.add_argument(
        "--deep",
        action="store_true",
        default=False,
        help="딥 크롤링 활성화 (기본값: False)",
    )
    deep_group.add_argument(
        "--depth",
        type=int,
        default=1,
        help="최대 크롤링 깊이 (기본값: 1)",
    )
    deep_group.add_argument(
        "--max-pages",
        type=int,
        default=10,
        help="크롤링할 최대 페이지 수 (기본값: 10)",
    )
    deep_group.add_argument(
        "--external",
        action="store_true",
        default=False,
        help="외부 도메인 포함 여부 (기본값: False)",
    )
    deep_group.add_argument(
        "--keywords",
        help="관련성 필터링을 위한 키워드 (쉼표로 구분)",
    )

    # 추출 설정
    extract_group = parser.add_argument_group("추출 설정")
    extract_group.add_argument(
        "--extract",
        choices=["none", "css", "llm", "default"],
        default="default",
        help="추출 전략 (기본값: default)",
    )
    extract_group.add_argument(
        "--llm-model",
        default="ollama/llama3",
        help="LLM 추출에 사용할 모델 (기본값: ollama/llama3)",
    )
    extract_group.add_argument(
        "--api-key",
        help="LLM API 키 (환경 변수가 없을 경우 필요)",
    )
    extract_group.add_argument(
        "--extract-schema",
        choices=["blog", "custom"],
        default="blog",
        help="추출 스키마 (기본값: blog)",
    )

    # 출력 설정
    output_group = parser.add_argument_group("출력 설정")
    output_group.add_argument(
        "--output-format",
        choices=["markdown", "json", "csv", "yaml"],
        default="markdown",
        help="출력 형식 (기본값: markdown)",
    )
    output_group.add_argument(
        "--output-dir",
        default="output",
        help="출력 디렉토리 (기본값: output)",
    )
    output_group.add_argument(
        "--save-images",
        action="store_true",
        default=False,
        help="이미지 정보 저장 여부 (기본값: False)",
    )
    output_group.add_argument(
        "--save-links",
        action="store_true",
        default=False,
        help="링크 정보 저장 여부 (기본값: False)",
    )
    output_group.add_argument(
        "--log-file",
        help="로그 파일 경로",
    )

    return parser


def parse_arguments(args=None):
    """
    명령줄 인수를 파싱합니다.

    Args:
        args: 명령줄 인수 (기본값: None, sys.argv[1:] 사용)

    Returns:
        argparse.Namespace: 파싱된 인수
    """
    parser = setup_argparse()
    parsed_args = parser.parse_args(args)

    # URL 또는 URL 목록 파일 중 하나는 반드시 제공되어야 함
    if not parsed_args.url and not parsed_args.url_list:
        parser.error("URL 또는 URL 목록 파일 중 하나는 반드시 제공해야 합니다.")

    # CacheMode 객체로 변환
    parsed_args.cache_mode = CacheMode(parsed_args.cache_mode)

    # 키워드 목록으로 변환
    if parsed_args.keywords:
        parsed_args.keywords = [k.strip() for k in parsed_args.keywords.split(",")]

    return parsed_args


def get_urls_from_args(args) -> List[str]:
    """
    인수에서 URL 목록을 가져옵니다.

    Args:
        args: 파싱된 인수

    Returns:
        List[str]: URL 목록
    """
    urls = []

    # 단일 URL 추가
    if args.url:
        urls.append(args.url)

    # URL 목록 파일에서 URL 추가
    if args.url_list:
        try:
            with open(args.url_list, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        urls.append(line)
        except Exception as e:
            print(f"URL 목록 파일 읽기 오류: {str(e)}")

    # 최대 URL 수 제한
    if args.max_urls > 0 and len(urls) > args.max_urls:
        urls = urls[: args.max_urls]

    return urls
