from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self):
        pass


class MCQQuestion(Question):
    def __init__(self, correct_answer, answer):
        self.correct_answer = correct_answer
        self.answer = answer

    def evaluate_answer(self):
        return self.answer == self.correct_answer


class TrueFalseQuestion(Question):
    def __init__(self, correct_answer, answer):
        self.correct_answer = correct_answer
        self.answer = answer

    def evaluate_answer(self):
        return self.answer == self.correct_answer


class DescriptiveQuestion(Question):
    def __init__(self, answer):
        self.answer = answer

    def evaluate_answer(self):
        if len(self.answer) >= 20:
            return True
        return False


q1 = MCQQuestion("B", "B")
q2 = TrueFalseQuestion(True, False)
q3 = DescriptiveQuestion("This is a descriptive answer with enough content.")

print("MCQ:", q1.evaluate_answer())
print("True/False:", q2.evaluate_answer())
print("Descriptive:", q3.evaluate_answer())