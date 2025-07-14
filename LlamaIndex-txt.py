from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import (
    DocxReader,
    HWPReader,
    PyMuPDFReader,
)
from pathlib import Path

reader = SimpleDirectoryReader(input_dir="./") # 폴더 내 파일 전체 로드됨
documents = reader.load_data()
 
print(documents)