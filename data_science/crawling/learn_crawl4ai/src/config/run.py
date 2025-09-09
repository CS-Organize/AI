from crawl4ai import CrawlerRunConfig


def setup_run_config(args, md_generator=None, extraction_strategy=None, deep_crawl_strategy=None):
    """
    크롤러 실행 설정을 구성합니다.

    Args:
        args: 명령줄 인수 객체
        md_generator: 마크다운 생성기 (기본값: None)
        extraction_strategy: 데이터 추출 전략 (기본값: None)
        deep_crawl_strategy: 딥 크롤링 전략 (기본값: None)

    Returns:
        CrawlerRunConfig: 크롤러 실행 설정 객체
    """
    config_params = {
        "word_count_threshold": 10,  # 최소 단어 수
        "cache_mode": args.cache_mode,  # 캐시 모드
        "wait_for": "domcontentloaded",  # 페이지 로드 기다리기 조건
        "screenshot": True,  # 스크린샷 캡처
        "pdf": True,  # PDF 변환
        "verbose": args.verbose,  # 상세 로깅
        "excluded_tags": ["nav", "aside", "footer", "form", "header"],  # 제외할 HTML 태그
        "exclude_external_links": True,  # 외부 링크 제외
        "remove_overlay_elements": True,  # 오버레이 요소 제거
        "process_iframes": True,  # iframe 처리
        "stream": args.stream if hasattr(args, "stream") else False,  # 스트리밍 모드
    }

    # 선택적 파라미터 추가
    if md_generator is not None:
        config_params["markdown_generator"] = md_generator

    if extraction_strategy is not None:
        config_params["extraction_strategy"] = extraction_strategy

    if deep_crawl_strategy is not None:
        config_params["deep_crawl_strategy"] = deep_crawl_strategy

    run_conf = CrawlerRunConfig(**config_params)

    # 사용자 지정 JS 코드 추가 (선택사항)
    if hasattr(args, "js_code") and args.js_code:
        run_conf.js_code = args.js_code

    # 사용자 지정 CSS 선택자 추가 (선택사항)
    if hasattr(args, "css_selector") and args.css_selector:
        run_conf.css_selector = args.css_selector

    # 세션 ID 추가 (선택사항)
    if hasattr(args, "session_id") and args.session_id:
        run_conf.session_id = args.session_id

    return run_conf


def setup_streaming_config(args, deep_crawl_strategy=None):
    """
    스트리밍 모드 설정을 구성합니다.

    Args:
        args: 명령줄 인수 객체
        deep_crawl_strategy: 딥 크롤링 전략 (선택사항)

    Returns:
        CrawlerRunConfig: 스트리밍 모드 설정 객체
    """
    config_params = {
        "word_count_threshold": 10,
        "cache_mode": args.cache_mode,
        "verbose": args.verbose,
        "excluded_tags": ["nav", "aside", "footer", "form", "header"],
        "exclude_external_links": True,
        "stream": True,  # 항상 스트리밍 활성화
    }

    if deep_crawl_strategy is not None:
        config_params["deep_crawl_strategy"] = deep_crawl_strategy

    return CrawlerRunConfig(**config_params)
