import meats
import os 
import time

from openai import OpenAI
from pprint import pprint
from random import randint

SEED = 123456789
with open(".env") as f:
    OPENAI_API_KEY = f.read().strip()

client = OpenAI(api_key=OPENAI_API_KEY)

all_meats = meats.COMMON_WESTERN_MEATS + meats.CONTROVERSIAL_MEATS + meats.CONTROL

if not os.path.exists('output'):
    os.makedirs('output')

for meat in all_meats:
    print(f"Processing {meat}...")
    if not os.path.exists(f'output/{meat}'):
        os.makedirs(f'output/{meat}')

    for n, prompt in enumerate(meats.PROMPTS):
        message = [
                   {"role": "system", "content": "You are a helpful assistant."},  # basically the default system context from the docs
                   {"role": "user", "content": prompt.format(meat)}
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=message,
            seed=SEED,
            max_tokens=100,
        )
        with open(f'output/{meat}/prompt{n}.txt', 'w') as f:
            f.write(response.choices[0].message.content)

        # openai api rate limit is pretty crazy but I still want to be nice
        time.sleep(randint(1, 5))

print("Done!")
