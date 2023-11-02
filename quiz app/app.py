# dictionary that stores the questions, choices, and answers
# Variable that tracks the player's scores
# Loop through the dictionary using the key value pairs
# display each quesion to the user and allow them to answer
# Tell them whether they got the question right or wrong
# show the final result when the quiz is completed

quiz = {
    "question1":{
        "question": " What company makes the Xperia model of smartphone?",
        "answer": "Sony"
    },
    "question2":{
        "question": "What is the name of the Android operating system?",
        "answer": "Marshmallow"
    },
    "question3":{
        "question": "Who is generally considered the inventor of the motor car?",
        "answer": "Karl Benz"
    },
    "question4":{
        "question": " What Italian city is famous for its system of canals?",
        "answer": "Venice"
    },
    "question5":{
        "question": "What is the capital of Australia?",
        "answer": "Canberra"
    },
    "question6":{
        "question": "What is Eminems real name? ",
        "answer": "Marshall Mathers"
    },
    "question7":{
        "question": "Sofia is the capital of what country?",
        "answer": "Bulgaria"
    }
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Enter your answer: ")
    if answer.lower() == value['answer'].lower():
        print("Correct!")
        score += 1
        print("Your score is ", str(score))
        
    else:
        print("Incorrect! The correct answer is ", value['answer'])
        print("Your score is ", str(score))
        
print("Your final score is ", str(score), "out of 7 questions correctly")
percentage = (score/7) * 100
print("Your percentage is ", str(percentage), "%")
   