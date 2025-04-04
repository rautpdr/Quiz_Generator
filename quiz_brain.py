class QuizBrain:
    #initilaising q_num as 0 and getting question list for further processing
    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    #next question function
    def next_question(self):
        #fetch the current question
        curr_question = self.q_list[self.q_num] #list[question_num]
        response = input(f"Q.{self.q_num} {curr_question.q_text}: ")
        self.q_num += 1
        self.check_ans(response , curr_question.q_ans)


    def check_ans(self , user_ans , correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You're Right!")
            print(f"Current Score = {self.score}\n")

        else:
            print("You're Wrong!")
            print(f"correct answer was {correct_ans}")
            print(f"Current Score = {self.score}\n")


    def q_exists(self , Data_size):
        #checking whether question exists or not
        if self.q_num < Data_size:
            return True
        else :
            return False