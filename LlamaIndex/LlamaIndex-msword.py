from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import (
    DocxReader,
    HWPReader,
    PyMuPDFReader,
)
from pathlib import Path

loader = DocxReader()
documents = loader.load_data(file=Path("./apply.docx"))
# C:\dev\workspace\py-project
 
print(documents)