import os
from openai import OpenAI


class LlmModel(object):
    def __init__(self, model, temperature) -> None:
        self.model = model
        self.temperature = temperature

    def request_chatgpt(self, prompt):
        client = OpenAI(
            # This is the default and can be omitted
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

        chat_completion = client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return chat_completion.choices[0].message.content

    def execute(self, prompt):
        # Request ChatGPT
        chatgpt_output = self.request_chatgpt(prompt)

        # remove lines of triple backticks
        prefix = "```"
        if chatgpt_output.startswith(prefix) and chatgpt_output.endswith(prefix):
            return self.remove_first_and_last_lines(chatgpt_output)
        return chatgpt_output

    def remove_first_and_last_lines(self, text):
        lines = text.splitlines()
        # Remove first and last lines
        if len(lines) >= 2:
            lines = lines[1:-1]
        else:
            # Return an empty string if there are not enough lines to remove
            return ''
        return '\n'.join(lines)