import re

# =====================================
# REILLY.AI SECURITY SYSTEM
# =====================================

class REILLYAISecurity:

    def __init__(self):

        self.inappropriate_words = [
            "badword1",
            "badword2",
            "badword3"
        ]

        self.blocked_messages = 0

    def check_message(self, message):

        # 1. Check phone numbers
        phone_pattern = (
            r'(?<!\d)(?:\+?1[-.\s]?)?'
            r'(?:\(?\d{3}\)?[-.\s]?)'
            r'\d{3}[-.\s]?\d{4}(?!\d)'
        )

        if re.search(phone_pattern, message):
            return self.block("Phone number detected")

        # 2. Check possible full names
        name_pattern = (
            r'\b[A-Z][a-z]{1,20}\s+'
            r'[A-Z][a-z]{1,20}\b'
        )

        if re.search(name_pattern, message):
            return self.block("Possible full name detected")

        # 3. Check inappropriate content
        words = re.findall(r'\b\w+\b', message.lower())

        for word in words:
            if word in self.inappropriate_words:
                return self.block("Inappropriate content detected")

        # Message approved
        return {
            "approved": True,
            "deleted": False,
            "reason": "Message approved"
        }

    def block(self, reason):

        self.blocked_messages += 1

        return {
            "approved": False,
            "deleted": True,
            "reason": reason
        }


# =====================================
# TEST SECURITY SYSTEM
# =====================================

security = REILLYAISecurity()

def process_message(message):

    result = security.check_message(message)

    if result["approved"]:
        print("SN AI: Message approved")
        return message

    else:
        print("REILLY.AI SECURITY ALERT!")
        print("Reason:", result["reason"])
        print("Message blocked and discarded.")

        return None


# =====================================
# TEST CHAT
# =====================================

if __name__ == "__main__":

    print("REILLY.AI SECURITY SYSTEM ONLINE")

    while True:

        message = input("\nEnter message (exit to stop): ")

        if message.lower() == "exit":
            break

        safe_message = process_message(message)

        if safe_message is not None:
            print("Approved message:", safe_message)

    print("\nTotal blocked messages:",
          security.blocked_messages)
