import string
import random as rand
import time
from pathlib import Path

FILE_NAME = "poem.txt"

base_dir = Path(__file__).resolve().parent
file_path = base_dir / FILE_NAME

init_character_list = " ".join("ᔑʖᓵ↸ᒷ⎓⊣⍑ᛁᕦᑑㄌᒲ∷𝙹!¡ᑑ∷ᓭℸ⚍⍊∴̇/||⨅").split()
speed = 0.01

try:
    with open(file_path, "r", encoding="utf-8") as file:
        for prompt in file:
            # Strips the newline from the end of each line in the txt file
            prompt = prompt.rstrip("\n")
            punctuation = [init_character_list[i % len(init_character_list)] for i in range(len(prompt)-1)]
            if prompt == "\n":
                print()
                continue
            
            for i in range(len(prompt)):
 
                # Prints the parts of the prompt that are revealed
                # and then the parts that are remaining with the random symbols
                print(f"\r{prompt[:i+1]} {''.join(punctuation[i:])}\033[K", end="", flush=True)

                rand.shuffle(punctuation)
                time.sleep(speed)

            # Little delay after each line is printed for cool dialogue effect
            time.sleep(0)
            print()

# Error handler for when the file is not found
except FileNotFoundError:
    print(f"Error: The file '{FILE_NAME}' was not found.")