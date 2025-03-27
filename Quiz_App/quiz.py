import random

# Quiz Data (Question, Options, Correct Answer Index)
quiz_data = [
    ("What is the keyword to define a function in Python?", ["func", "define", "def", "lambda"], 2),
    ("Which movie won the Oscar for Best Picture in 2023?", ["Avatar 2", "Top Gun: Maverick", "Everything Everywhere All at Once", "The Batman"], 2),
    ("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], 2),
    ("Which data structure uses LIFO?", ["Queue", "Stack", "Heap", "Linked List"], 1),
    ("Who directed 'Inception'?", ["Christopher Nolan", "Steven Spielberg", "Quentin Tarantino", "James Cameron"], 0)
]

def run_quiz():
    score = 0
    random.shuffle(quiz_data)  # Shuffle questions for variation

    for i, (question, choices, correct_index) in enumerate(quiz_data, start=1):
        print(f"\nQ{i}: {question}")
        for j, option in enumerate(choices, start=1):
            print(f"  {j}. {option}")

        while True:
            try:
                answer = int(input("Your answer (1-4): ")) - 1
                if 0 <= answer < 4:
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Enter a number.")

        if answer == correct_index:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {choices[correct_index]}")

    print(f"\n🏆 Quiz Complete! Your final score: {score}/{len(quiz_data)}")

while True:
    run_quiz()
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing! 🎮")
        break
