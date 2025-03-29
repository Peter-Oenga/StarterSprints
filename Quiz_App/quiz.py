import random

quiz_data = [
    ("What is the capital City of Kenya", ["Nairobi", "Mombasa", "Kisumu", "Kisii"], 0),
    ("Which county is the richest", ["Machakos", "Kisii", "Laikipia", "Mandera"], 1),
    ("How old am I", [12, 23,43,12], 1),
    ("Who is the richest man in the World", ["Elon Musk", "Jeff Bezos", "Jack Ma", "William Ruto"], 0),
    ("What is the capital city of Africa", ["Cape Town", "Kampala", "Nairobi", "Dodoma"], 2)
]

def run_quiz():
    score = 0
    random.shuffle(quiz_data)

    for i, (question, choices, correct_index) in enumerate(quiz_data, start=1):
        print(f"\nQ{i}: {question}")

        for j, option in enumerate(choices, start=1):
            print(f"{j} :{option}")
        
        while True:
            try:
                answer = int(input("Enter an anwer between 1 and 4: ")) - 1

                if 0 <= answer < 4:
                    break
                else:
                    print("Please input an option between 1 - 4")
            except ValueError:
                print("Please enter a valid number")

        if answer == correct_index:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {choices[correct_index]}")
        
    print(f"Your total score is {score}/{len(quiz_data)}")


    
while True:
    run_quiz()
    again = input("Do you want to play again? (yes/No) ").strip().lower()

    if again != "yes":
        print("Thanks for playing")
        break


