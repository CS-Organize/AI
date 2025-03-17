from crawl4ai import CrawlerRunConfig


def setup_run_config(args, md_generator):
    run_conf = CrawlerRunConfig(
        word_count_threshold=10,  # Minimum words per content block
        # extraction_strategy=None,
        markdown_generator=md_generator,
        cache_mode=args.cache_mode,
        # js_code=None,
        wait_for="js:() => window.loaded === true",
        screenshot=True,
        pdf=True,
        verbose=False,  # Same as browser_conf.verbose
        excluded_tags=["form", "header"],
        exclude_external_links=True,  # Remove external links
        remove_overlay_elements=True,  # Remove popups/modals
        process_iframes=True,  # Process iframe content
    )
    return run_conf
