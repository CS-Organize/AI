import asyncio

from crawl4ai import AsyncWebCrawler, CacheMode, CrawlerRunConfig


async def main():
    config = CrawlerRunConfig(
        word_count_threshold=20,
        excluded_tags=["nav", "footer", "header"],
        exclude_external_links=True,
        exclude_social_media_links=True,
        exclude_external_images=True,
        cache_mode=CacheMode.ENABLED,
    )

    # Create an instance of AsyncWebCrawler
    async with AsyncWebCrawler() as crawler:
        # Run the crawler on a URL
        result = await crawler.arun(
            url="https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide", config=config
        )

        with open("output.md", "w") as f:
            f.write(result.markdown)


# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
