# Here I learn how to use classes and objects via building a multiple choice quiz

from Class import Question

questions = ["1. Question1 \na)haha \nb)huh \nc)uhd\n",
             "2. Question2 \na)haha \nb)huh \nc)uhd\n",
             "3. Question3 \na)haha \nb)huh \nc)uhd\n"
             ]


quiz = [Question(questions[0], "a"),
        Question(questions[1], "b"),
        Question(questions[2], "c"),
        ]

def run_quiz(quiz):
    score = 0
    for question in quiz:
        prompt = input(question.prompt)
        if prompt == question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(quiz)) + ' correct!')


run_quiz(quiz)
