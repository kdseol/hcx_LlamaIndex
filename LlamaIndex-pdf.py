from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import (
    DocxReader,
    HWPReader,
    PyMuPDFReader,
)
from pathlib import Path

loader = PyMuPDFReader()
documents = loader.load(file_path=Path("./apply.pdf"))


for doc in documents:
    print(doc.metadata)
    print(doc.text[:300])  # 미리보기
