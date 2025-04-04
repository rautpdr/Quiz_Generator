from question_model import QuestionModel
from data import quiz_data
from quiz_brain import  QuizBrain

#create a question_bank

question_bank = []
for q in quiz_data:
    question = q["question"]
    answer = q["answer"]
    new_question = QuestionModel(question , answer)
    question_bank.append(new_question)

q_brain = QuizBrain(question_bank)


while q_brain.q_exists(len(quiz_data)):
    q_brain.next_question()

print("Thanks for playing!!!")
