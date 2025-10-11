import sys
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


from backend.ingestion.pdf_loader_V2 import data_loader
from backend.ingestion.meta_data_ingestion import metadata_ingested_docs
x = data_loader('backend\ingestion\Sentiment analysis in Bengali via transfer learning.pdf',
              extract_images=True)


x = metadata_ingested_docs(x,"gemini-2.5-flash-lite")

print(type(x))
print(x)
#hello
