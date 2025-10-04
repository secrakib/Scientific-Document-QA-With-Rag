import sys
from pathlib import Path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pipeline.pipeline import pipeline

# Chat with the bot
session_id = "1"



result = pipeline('backend\ingestion\Sentiment analysis in Bengali via transfer learning.pdf'
                  ,session_id,
                  "What question I have asked you first?")

print(result['answer'])
#print(result)
'''# Query 1
result1 = pipeline.invoke(
    {"input": "What ML models are used?"},
    config={"configurable": {"session_id": session_id}}
)
print(f"Answer 1: {result1['answer']}\n")
print(result1)

# Query 2 - remembers previous context
result2 = pipeline.invoke(
    {"input": "Tell me more about these models"},
    config={"configurable": {"session_id": session_id}}
)
print(f"Answer 2: {result2['answer']}\n")

# Query 3
result3 = pipeline.invoke(
    {"input": "What are their accuracy scores?"},
    config={"configurable": {"session_id": session_id}}
)
print(f"Answer 3: {result3['answer']}\n")'''