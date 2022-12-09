from Quizes import Quizzes
from Question_request import Question


def Ask_question1(question_quiz1):
    Score = 0
    for question in question_quiz1:
        answer = input(question.Question_request)
        if answer == question.answer:
            Score += 1
    quizzes[0].evaluation.append(Score)
    return quizzes[0].evaluation



def Ask_question2(question_quiz2):
    Score = 0
    for question in question_quiz2:
        answer = input(question.Question_request)
        if answer == question.answer:
            Score += 1
    quizzes[1].evaluation.append(Score)
    return quizzes[1].evaluation



def Message (Asq_question1, Asq_question2, evaluation):
    pass




Quizes = ["quiz1", "quiz2"]

Question_request_1=["Which of this country is in Africa?\n(a) Egypt \n(b) Sweden \n(c)Germany \n(d)Russia\n",
        "All of this is a continent except?\n(a) Africa \n(b) Europe \n(c)Asia \n(d) Germany\n",
        "Which of this is a country in Europe?\n(a)USA \n(b) Cameroun \n(c)Germany \n(d) Canada\n"
        ]

Question_request_2= ["Which of this ,is a programming language?\n(a)Tableau \n(b)Visual basic \n(c) Python \n(d) Mongol db\n",
         "Which of this is not a data base management system?\n(a)MongolDB \n(b)MySQl \n(c)SQLite \n(d)Tensorflow\n",
         "The following is a computer part except?\n(a)keyboard \n(b)Bluetooth \n(c)Mouse \n(d)Monitor\n"
         ]

quizzes = [
    Quizzes(Quizes[0], evaluation=[]),
    Quizzes(Quizes[1], evaluation=[])
]



question_quiz1 = [Question(Question_request_1[0], "a"),
                  Question(Question_request_1[1], "d"),
                  Question(Question_request_1[2], "c")
                  ]

question_quiz2 = [Question(Question_request_2[0], "c"),
                  Question(Question_request_2[1], "d"),
                  Question(Question_request_2[2], "b")
                  ]


Quiz_test_1 = Ask_question1(question_quiz1)
Quiz_test_2 = Ask_question2(question_quiz2)


    
    

        




