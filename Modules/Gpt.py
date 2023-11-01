import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
import json

class Gpt:
    @staticmethod
    def calcDistance(cityA, cityB):
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "Generate road length in kilometers between 2 cities A and B in json file. only variable=length"},
            {"role": "user", "content": f"A={cityA}, B={cityB}"}
        ])
        length = json.loads(completion.choices[0].message.content)
        print(length["length"], 'KM')


Gpt.calcDistance("Warsaw", "Berlin")