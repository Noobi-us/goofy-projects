import string
import random as rand
import time
from pathlib import Path

FILE_NAME = "poem.txt"

base_dir = Path(__file__).resolve().parent

file_path = base_dir / FILE_NAME

punctuation = list(string.punctuation)
speed = 0.05
try:
    with open(file_path, "r", encoding="utf-8") as file:
        for prompt in file:
            
            if prompt == "\n":
                print()
                continue

            for i in range(len(prompt)):
                punctuation = [punctuation[i % len(punctuation)] for i in range(len(prompt)-1)]
                print(f"\r{prompt[:i+1]} {str("".join(punctuation[i+1:]))}", end="", flush=True)
                rand.shuffle(punctuation)
                time.sleep(speed)

except FileNotFoundError:
    print(f"Error: The file '{FILE_NAME}' was not found.")