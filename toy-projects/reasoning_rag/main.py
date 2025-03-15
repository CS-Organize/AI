from typing import Annotated, List, Literal, TypedDict

from IPython.display import Markdown, display
from langchain_core.documents import Document
from langchain_docling.loader import DoclingLoader, ExportType
from langchain_ollama import ChatOllama
from langgraph.graph.message import add_messages

reasoning_llm = ChatOllama(model="jinbora/deepseek-r1-Bllossom:8b", stop=["</think>"])
answer_llm = ChatOllama(model="exaone3.5", temperature=0)


class RAGState(TypedDict):
    query: str
    thinking: str
    documents: List[Document]
    answer: str
    messages: Annotated[List, add_messages]
    mode: str


FILE_PATH = "https://arxiv.org/pdf/2408.09869"

loader = DoclingLoader(file_path=FILE_PATH, export_type=ExportType.MARKDOWN)
docs = loader.load()


def main():
    print(docs)


if __name__ == "__main__":
    main()
