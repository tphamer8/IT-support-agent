'''
  password_reset
  login_troubleshooting
  access_request
  vpn_support
  ticket_summary
  escalation
  unknown
  
'''

class IntentClassifier:
    def __init__(self) -> None:
        self.default_intent = "unknown"
        self.intent_keywords = {
            "ticket_summary": ["ticket", "summary", "summarize"],
            "escalation": ["escalation", "escalated", "escalate"],
            "vpn_support": ["vpn", "network", "connection", "connectivity"],
            "access_request": ["access request", "request access", "permission"],
            "login_troubleshooting": ["login", "log in", "sign in", "troubleshoot"],
            "password_reset": ["password", "reset", "forgot", "locked out"],
        }

    def classify(self, user_input: str) -> str:

        user_input_lower = user_input.lower()

        for intent, keywords in self.intent_keywords.items():
            if any(word in user_input_lower for word in keywords):
                return intent

        return self.default_intent

