import sys
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))




from backend.ingestion.pdf_loader_V2 import data_loader
x=data_loader(path='C:\Langchain\Scientific-Pdf-Rag\backend\ingestion\Sentiment analysis in Bengali via transfer learning.pdf',
              extract_images=True)
print(x)
#hello
