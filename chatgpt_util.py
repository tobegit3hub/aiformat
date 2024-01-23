import os
from openai import OpenAI

def request_chatgpt(prompt):
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    #print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content
