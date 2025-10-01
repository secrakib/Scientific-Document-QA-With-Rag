import sys
import os

# Add the parent directory to Python path
backend_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if backend_parent not in sys.path:
    sys.path.insert(0, backend_parent)

