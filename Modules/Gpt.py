from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

import json

class Gpt:
    @staticmethod
    def calcDistance(cityA, cityB):
        completion = client.chat.completions.create(model="gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "Generate road length in kilometers between 2 cities A and B in json file. only variable=length"},
            {"role": "user", "content": f"A={cityA}, B={cityB}"}
        ])
        content = json.loads(completion.choices[0].message.content)
        print(content["length"], 'KM')


Gpt.calcDistance("Kraków", "Smyków")