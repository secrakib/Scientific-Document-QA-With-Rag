import sys
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv
load_dotenv()

import os

from backend.ingestion.pdf_loader_V2 import data_loader
from backend.ingestion.meta_data_ingestion import metadata_extraction
x = data_loader(path='backend\ingestion\Sentiment analysis in Bengali via transfer learning.pdf',api_key=os.getenv('GOOGLE_API_KEY'),
              model="gemini-2.5-flash-lite",extract_images=True)


x = metadata_extraction(x,os.getenv('GOOGLE_API_KEY'),"gemini-2.5-flash-lite")

print(x)
#hello
