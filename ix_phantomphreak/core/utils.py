"""
IX-PhantomPhreak Utilities Module

Helper functions for cleaning and validating networking and communications queries.
"""

import re

def clean_query(query: str) -> str:
    """
    Normalize the input query by trimming whitespace and removing
    non-alphanumeric characters except essential symbols.
    """
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    query = re.sub(r'[^\w\s\-\+\=\(\)\[\]\.:]+', '', query)
    return query

def is_valid_query(query: str) -> bool:
    """
    Basic validation to ensure query contains meaningful characters.
    """
    return bool(query and len(query) > 3 and any(c.isalpha() for c in query))

# Example usage
if __name__ == "__main__":
    tests = [
        "   What is TCP/IP?   ",
        "!!!",
        "Latency",
        "Explain router!"
    ]
    for q in tests:
        cleaned = clean_query(q)
        valid = is_valid_query(cleaned)
        print(f"'{q}' → Cleaned: '{cleaned}' | Valid: {valid}")
