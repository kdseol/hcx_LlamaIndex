from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import (
    DocxReader,
    HWPReader,
    PyMuPDFReader,
)
from pathlib import Path

parser = DocxReader()
file_extractor = {".docx": parser}
documents = SimpleDirectoryReader(
    "/dev/workspace/py-project/", file_extractor=file_extractor
).load_data()
 
for doc in documents:
    print(doc)