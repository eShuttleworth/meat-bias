import os

from pprint import pprint

results = {}
for meat in os.listdir('output'):
    results[meat] = {}
    results[meat]['responses'] = []
    for prompt in os.listdir(f'output/{meat}'):
        with open(f'output/{meat}/{prompt}') as f:
            results[meat]['responses'].append(f.read().strip())
for meat in results:
    for response in results[meat]['responses']:
        if "I'm sorry" in response:
            print(f"{meat} are controversial.")

print(results)