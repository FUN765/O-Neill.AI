import os
from typing import TypedDict
from openai import OpenAI


class AIResponse(TypedDict):
    text: str
    error: str | None


class AIAssistant:
    def __init__(self, model: str = "gpt-4.1-mini"):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("Set the OPENAI_API_KEY environment variable")

        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.messages: list[dict[str, str]] = [
            {
                "role": "system",
                "content": "You are a helpful, concise AI assistant.",
            }
        ]

    def ask(self, user_message: str) -> AIResponse:
        user_message = user_message.strip()
        if not user_message:
            return {"text": "", "error": "Message cannot be empty"}

        self.messages.append({"role": "user", "content": user_message})

        try:
            response = self.client.responses.create(
                model=self.model,
                input=self.messages,
            )

            answer = response.output_text
            self.messages.append({"role": "assistant", "content": answer})
            return {"text": answer, "error": None}

        except Exception as error:
            # Remove the failed user message so it can be retried.
            self.messages.pop()
            return {"text": "", "error": str(error)}

    def reset(self) -> None:
        self.messages = self.messages[:1]


def main() -> None:
    assistant = AIAssistant()

    print("AI Assistant ready. Type 'exit' or 'reset'.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            break
        if user_input.lower() == "reset":
            assistant.reset()
            print("Conversation reset.")
            continue

        result = assistant.ask(user_input)

        if result["error"]:
            print(f"Error: {result['error']}")
        else:
            print(f"AI: {result['text']}")


if __name__ == "__main__":
    main()
