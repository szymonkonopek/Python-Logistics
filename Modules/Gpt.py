import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key="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")

import json

class Gpt:
    @staticmethod
    def calcDistance(cityA, cityB):
        completion = client.chat.completions.create(model="gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "Generate road length in kilometers between 2 cities A and B in json file. only variable=length"},
            {"role": "user", "content": f"A={cityA}, B={cityB}"}
        ])
        length = json.loads(completion.choices[0].message.content)
        print(length["length"], 'KM')


Gpt.calcDistance("Warsaw", "Berlin")