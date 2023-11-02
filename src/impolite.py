import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

while True:
    user_input = input("put your description here...")
    if user_input == 'quit':
        break

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You can identify impolite customers. If the person was impolite flag the conversation by saying 'impolite'."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=150,
    )

    response_message = response["choices"][0]["message"]['content']
    if response_message.lower() == 'impolite':
        break
    print(response_message)
