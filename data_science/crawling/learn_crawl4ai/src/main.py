import asyncio

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

from config.browser import setup_browser_config
from config.markdown import setup_markdown_generator
from config.run import setup_run_config
from utils.arg import setup_argparse
from utils.file import save_png_to_unique_file, save_text_to_unique_file

urls = [
    "https://www.ag-grid.com/react-data-grid/",
]


async def main():
    parser = setup_argparse()
    args = parser.parse_args()

    browser_conf = setup_browser_config(args)
    md_generator = setup_markdown_generator()
    run_conf = setup_run_config(args, md_generator)
    async with AsyncWebCrawler(config=browser_conf) as crawler:
        result = await crawler.arun(url=args.url, run_config=run_conf)

        if result.screenshot:
            save_png_to_unique_file(result.screenshot, "screenshot")

        if result.success:
            # Print clean content
            md_obj = result.markdown
            print("Raw Markdown length:", len(md_obj.raw_markdown))
            print("Fit Markdown length:", len(md_obj.fit_markdown))

            # # Process images
            # for image in result.media["images"]:
            #     print(f"Found image: {image['src']}")

            # # Process links
            # for link in result.links["internal"]:
            #     print(f"Internal link: {link['href']}")

            save_text_to_unique_file(md_obj)

        else:
            print(f"Crawl failed: {result.error_message}")


if __name__ == "__main__":
    asyncio.run(main())
