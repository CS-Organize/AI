from crawl4ai import BrowserConfig


def setup_browser_config(args):
    browser_conf = BrowserConfig(
        browser_type="chromium",
        headless=args.headless,
        # proxy_config=None,
        viewport_width=1080,
        viewport_height=600,
        verbose=args.verbose,
        use_persistent_context=True,
        user_data_dir="data",
        # cookies=None,
        # headers=None,
        # user_agent=None,
        text_mode=False,
        light_mode=False,
        # extra_args=None,
    )

    return browser_conf
