from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import (
    DocxReader,
    HWPReader,
    PyMuPDFReader,
)
from pathlib import Path

hwp_path = Path("/dev/workspace/py-project/apply.hwp")
reader = HWPReader()
documents = reader.load_data(file=hwp_path)
 
print(documents)