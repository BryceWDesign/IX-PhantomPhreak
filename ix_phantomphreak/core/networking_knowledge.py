"""
IX-PhantomPhreak Core Networking Knowledge Module

Contains essential definitions and concepts related to computer networking,
internet protocols, signal processing, and communication technologies.

Part of the IX-Gibson sibling AI network.
"""

class NetworkingKnowledge:
    def __init__(self):
        self.facts = {
            "tcp/ip": "A suite of communication protocols used to interconnect network devices on the internet.",
            "udp": "A communications protocol that is primarily used for establishing low-latency and loss-tolerating connections.",
            "http": "An application protocol for distributed, collaborative, hypermedia information systems, foundational to the World Wide Web.",
            "dns": "The Domain Name System translates domain names to IP addresses allowing browsers to load internet resources.",
            "firewall": "A network security system that monitors and controls incoming and outgoing network traffic based on security rules.",
            "router": "A networking device that forwards data packets between computer networks.",
            "latency": "The delay from input into a system to the desired outcome, crucial in networking and communications.",
            "packet switching": "A method of grouping data transmitted over a digital network into packets."
        }

    def get_fact(self, term: str) -> str:
        term_lower = term.lower().strip()
        return self.facts.get(term_lower, f"Sorry, I don't yet have information on '{term}'.")

# Example test
if __name__ == "__main__":
    nk = NetworkingKnowledge()
    print(nk.get_fact("TCP/IP"))
    print(nk.get_fact("DNS"))
    print(nk.get_fact("Quantum networking"))
