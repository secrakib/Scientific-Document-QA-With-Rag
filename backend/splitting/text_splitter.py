import sys
from pathlib import Path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))


from backend.ingestion.pdf_loader import data_loader
print(data_loader(r'backend\ingestion\Sentiment analysis in Bengali via transfer learning.pdf'))
