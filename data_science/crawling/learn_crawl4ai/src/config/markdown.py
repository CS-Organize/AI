from crawl4ai.content_filter_strategy import BM25ContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


def setup_markdown_generator():
    md_generator = DefaultMarkdownGenerator(
        options={
            "ignore_links": True,
            "ignore_images": True,
            "escape_html": False,
            "body_width": 80,
            "skip_internal_links": True,
            "include_sup_sub": True,
        }
    )
    return md_generator
