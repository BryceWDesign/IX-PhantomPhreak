"""
IX-PhantomPhreak CLI Tool

Interactive command line interface for manual input scanning,
log inspection, and real-time exploit detection.
"""

from core.exploit_detector import ExploitDetector
from core.event_logger import EventLogger

def main():
    detector = ExploitDetector()
    logger = EventLogger()

    while True:
        print("\n--- IX-PhantomPhreak CLI ---")
        print("1. Scan input for exploits")
        print("2. View recent logs")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            source = input("Enter source ID: ").strip()
            content = input("Enter input content: ").strip()
            patterns = detector.scan_input(content)
            if patterns:
                logger.log_event(source, content, patterns)
                print(f"[ALERT] Exploit detected: {patterns}")
            else:
                print("[OK] No exploits detected.")

        elif choice == "2":
            logs = logger.get_recent_events()
            if not logs:
                print("No logs available.")
            else:
                for event in logs:
                    print(f"- Time: {event['timestamp']}, Source: {event['source']}, Patterns: {event['patterns_detected']}")

        elif choice == "3":
            print("Exiting IX-PhantomPhreak CLI.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
