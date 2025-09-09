from crawl4ai import BrowserConfig


def setup_browser_config(args):
    """
    브라우저 설정을 구성합니다.

    Args:
        args: 명령줄 인수 객체

    Returns:
        BrowserConfig: 브라우저 설정 객체
    """
    # user_agent가 None이면 기본값 사용
    default_ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    user_agent = default_ua
    if hasattr(args, "user_agent") and args.user_agent:
        user_agent = args.user_agent

    browser_conf = BrowserConfig(
        browser_type=args.browser,  # 브라우저 유형 (chromium, firefox, webkit)
        headless=args.headless,  # 헤드리스 모드 여부
        viewport_width=1080,
        viewport_height=800,
        verbose=args.verbose,  # 상세 로깅 여부
        use_persistent_context=True,  # 세션 유지
        user_data_dir="data",  # 사용자 데이터 디렉토리
        text_mode=False,  # 텍스트 모드 (이미지 비활성화)
        light_mode=False,  # 라이트 모드 (리소스 제한)
        java_script_enabled=True,  # 자바스크립트 활성화
        user_agent=user_agent,  # 사용자 에이전트
    )

    return browser_conf


def setup_mobile_browser_config(args):
    """
    모바일 브라우저 설정을 구성합니다.

    Args:
        args: 명령줄 인수 객체

    Returns:
        BrowserConfig: 모바일 브라우저 설정 객체
    """
    mobile_user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"

    browser_conf = BrowserConfig(
        browser_type="chromium",
        headless=args.headless,
        viewport_width=375,  # 모바일 뷰포트 너비
        viewport_height=812,  # 모바일 뷰포트 높이
        verbose=args.verbose,
        use_persistent_context=True,
        user_data_dir="data/mobile",
        user_agent=mobile_user_agent,
        text_mode=False,
        light_mode=False,
        java_script_enabled=True,
    )

    return browser_conf
