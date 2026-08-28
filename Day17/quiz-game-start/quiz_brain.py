class QuizBrain:
    def __init__(self,q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def NextQuestion(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        global quiz
        quiz = input(f"Q.{self.question_number}: {question.text} (True/False)").lower()
        correct_answer = question.answer
        self.check_answer(quiz,correct_answer)
        print("\n")
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You Got it!")
            self.score += 1
        else:
            print("WRONG")
        print(f"The Correct answer is: {correct_answer}")
        print(f"Your Score: {self.score}/{self.question_number}")
        self.final_score(self.score,self.question_number)
        
    def final_score(self, correct, total):
        if self.question_number == len(self.question_list):
            print("\n You've Completed the quiz")
            print(f"Your Score: {self.score}/{self.question_number}")