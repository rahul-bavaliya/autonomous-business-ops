from typing import List, Dict


class ConversationMemory:

    def __init__(self):

        self.messages: List[Dict] = []

    def add_user_message(
        self,
        content: str
    ):

        self.messages.append(
            {
                "role": "user",
                "content": content
            }
        )

    def add_assistant_message(
        self,
        content: str
    ):

        self.messages.append(
            {
                "role": "assistant",
                "content": content
            }
        )

    def get_history(
        self
    ) -> List[Dict]:

        return self.messages

    def clear(
        self
    ):

        self.messages = []