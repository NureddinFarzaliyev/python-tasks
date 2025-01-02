import json
import random

isRunning = True

with open('output_questions.json', 'r') as f:
    questions_data = json.load(f)
    while isRunning:
        random_number = random.randint(0, len(questions_data) - 1)
        print("\n" + questions_data[random_number]['question'] + "\n")

        for choice in questions_data[random_number]['choices']:
            print("-" + choice[1:].strip())

        input("\n>>> press enter to see the right answer\n")

        for choice in questions_data[random_number]['choices']:
            print("-" + choice)

        quit = input("\n>>> press enter to continue or q + enter to stop\n")
        if(quit == "q" or quit == "Q"): isRunning = False
        else: print("\n----------------------------------------------------------------\n")
