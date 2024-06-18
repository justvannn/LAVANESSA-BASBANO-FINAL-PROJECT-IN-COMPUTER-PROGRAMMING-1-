print("Number 2.")
import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.total_questions = len(questions)
        self.current_question_index = 0
        self.score = 0
        self.user_answers = [None] * self.total_questions
    
    def display_question(self):
        print(f"Question {self.current_question_index + 1}:")
        print(self.questions[self.current_question_index]['question'])
    
    def check_answer(self, answer):
        correct_answer = self.questions[self.current_question_index]['answer']
        if answer.lower() == correct_answer.lower():
            self.score += 1
        self.user_answers[self.current_question_index] = answer
    
    def display_results(self):
        print("Quiz Results:")
        print(f"Total questions: {self.total_questions}")
        print(f"Your score: {self.score}/{self.total_questions}\n")
        
        print("Review Answers:")
        for i, question in enumerate(self.questions):
            print(f"Question {i + 1}: {question['question']}")
            print(f"Your Answer: {self.user_answers[i]}")
            print(f"Correct Answer: {question['answer']}\n")
    
    def run_quiz(self):
        random.shuffle(self.questions)
        
        print("Welcome to the Quiz!")
        print("Type your answer and press Enter to submit.")
        input("Press Enter to start the quiz...")
        
        while self.current_question_index < self.total_questions:
            self.display_question()
            user_answer = input("Your answer: ")
            self.check_answer(user_answer)
            self.current_question_index += 1
        
        print("\nQuiz completed!")
        
questions_data = [{'question': "What is the capital of France?",'answer': "Paris" },{'question': "Who wrote 'Hamlet'?",'answer': "William Shakespeare"},]

quiz = Quiz(questions_data)

quiz.run_quiz()
