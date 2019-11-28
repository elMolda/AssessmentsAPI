class Question:
    def __init__(self, id, text, isOpen):
        self.id = id
        self.text = text
        self.isOpen = isOpen

    def qstnToJson(self):
        return({'Question Id': self.id,
                'Question Text': self.text,
                'Is Open': str(self.isOpen)})