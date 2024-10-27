import json
import requests
import random

url = "https://raw.githubusercontent.com/Katherine-Brown-8000/Hiragana_flash_cards/refs/heads/main/Hiragana.json"
response = requests.get(url)

if response.status_code == 200:
    hiragana = json.loads(response.text)
else:
    print("failed to retrieve the data")

q_count = int(input("enter the number of flash cards you would like to do: "))

def score_hiragana():
    score = 0

    for i in range(q_count):
        char, correct_answer = random.choice(list(hiragana.items()))

        answer = input(f"What is {char}:")

        if isinstance(correct_answer, list):
            correct_answers_lower = [ans.lower() for ans in correct_answer]
            if answer.lower() in correct_answers_lower:
                score += 1

        else:
            if answer.lower() == correct_answer.lower():
                score += 1

    total_score = (score / q_count ) * 100
    return total_score

total = score_hiragana()
print(f"Your score is: {total}")
