import requests
import pprint
import random
# pip install requests
trivia_url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy"

response = requests.get(trivia_url)
data = response.json()
pprint.pprint(data)

for q in data['results']:
    print(q['question'], end="\n--------")
    correct_answer = q['correct_answer']
    all_answers = q['incorrect_answers'] + [correct_answer]
    random.shuffle(all_answers)
    answers_dict = {i+1:answer for i, answer in enumerate(all_answers)}
    print("Answers:")
    for i, a in enumerate(all_answers):
        print(f"{i+1}.{a}")
    user_answer_num = int(input("Your answer: "))
    user_answer = answers_dict[user_answer_num]
    if user_answer == correct_answer:
       print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_answer}")