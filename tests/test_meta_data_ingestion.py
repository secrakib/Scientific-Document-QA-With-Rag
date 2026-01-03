import sys
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


from backend.ingestion.pdf_loader_V2 import data_loader
from backend.ingestion.meta_data_ingestion import metadata_ingested_docs
x = data_loader(r'backend/ingestion/Sentiment analysis in Bengali via transfer learning.pdf',
              extract_images=False)


x = metadata_ingested_docs(x,"openai/gpt-oss-120b")

print(type(x))
print(x)

