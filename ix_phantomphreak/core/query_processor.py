"""
IX-PhantomPhreak Domain-Specific Query Processor

Handles queries related to networking, internet protocols,
communications technologies, and signal processing.
"""

from networking_knowledge import NetworkingKnowledge

class IXPhantomPhreakQueryProcessor:
    def __init__(self):
        self.knowledge = NetworkingKnowledge()

    def process_query(self, query: str) -> str:
        query_lower = query.lower().strip()

        if query_lower.startswith("what is "):
            term = query_lower[8:].strip()
            return self.knowledge.get_fact(term)
        elif "define" in query_lower:
            term = query_lower.split("define")[-1].strip()
            return self.knowledge.get_fact(term)
        elif "explain" in query_lower:
            term = query_lower.split("explain")[-1].strip()
            return self.knowledge.get_fact(term)
        else:
            return (
                "I am IX-PhantomPhreak, your networking and communications specialist. "
                "Ask me to define or explain any networking or internet concept."
            )

# Example usage
if __name__ == "__main__":
    processor = IXPhantomPhreakQueryProcessor()
    print(processor.process_query("What is TCP/IP?"))
    print(processor.process_query("Define router"))
    print(processor.process_query("Explain latency"))
