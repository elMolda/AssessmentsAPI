import Entities.Answer
class Question:
    def __init__(self, id, text, isOpen):
        self.id = id
        self.text = text
        self.isOpen = isOpen
        self.answers = []

    def qstnToJson(self):
        answersJson = []
        for a in self.answers:
            answersJson.append(a.answrToJson())
        return({'Question Id': self.id,
                'Question Text': self.text,
                'Is Open': str(self.isOpen),
                'Answers': answersJson})