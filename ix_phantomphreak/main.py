"""
IX-PhantomPhreak CLI Entry Point

Enables terminal-based queries for networking and communications knowledge.
Outputs results directly to the command line.
"""

import sys
from core.query_processor import IXPhantomPhreakQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your networking question here\"")
        sys.exit(1)

    query = sys.argv[1]
    processor = IXPhantomPhreakQueryProcessor()
    response = processor.process_query(query)

    print("\n🌐 IX-PhantomPhreak Response 🌐")
    print(response)

if __name__ == "__main__":
    main()
