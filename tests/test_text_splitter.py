import sys
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from backend.ingestion.pdf_loader import data_loader
from backend.splitting.text_splitter import text_splitter


a = data_loader(r'backend\ingestion\Sentiment analysis in Bengali via transfer learning.pdf')
b = text_splitter(a)

print(b)

