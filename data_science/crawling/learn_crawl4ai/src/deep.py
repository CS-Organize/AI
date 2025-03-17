import asyncio

from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig

from utils.arg import setup_argparse
from utils.file import save_text_to_unique_file

urls = [
    "https://www.ag-grid.com/react-data-grid/",
]

from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.deep_crawling.scorers import KeywordRelevanceScorer

# Create a scorer


# Configure the strategy


async def main():
    parser = setup_argparse()
    args = parser.parse_args()
    browser_conf = BrowserConfig(headless=args.headless, verbose=args.verbose)
    # Basic configuration
    strategy = BFSDeepCrawlStrategy(
        max_depth=2,  # Crawl initial page + 2 levels deep
        include_external=False,  # Stay within the same domain
        max_pages=1,  # Maximum number of pages to crawl (optional)
    )
    run_conf = CrawlerRunConfig(
        word_count_threshold=10,  # Minimum words per content block
        excluded_tags=["form", "header"],
        exclude_external_links=True,  # Remove external links
        remove_overlay_elements=True,  # Remove popups/modals
        process_iframes=True,  # Process iframe content
        deep_crawl_strategy=strategy,
        verbose=True,
        cache_mode=CacheMode.ENABLED,
        stream=True,
    )
    async with AsyncWebCrawler(config=browser_conf) as crawler:
        async for result in await crawler.arun(url=args.url, config=run_conf):
            # Process each result as it becomes available
            print("*" * 80)
            print(result)
            print("*" * 80)
            if result.success:
                # Print clean content
                print("Content:", result.markdown[:500])  # First 500 chars
                save_text_to_unique_file(str(result))
            else:
                print(f"Crawl failed: {result.error_message}")


if __name__ == "__main__":
    asyncio.run(main())
