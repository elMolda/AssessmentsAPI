class Answer:
    def __init__(self, id, answerText, question_id):
        self.id = id
        self.answerText = answerText
        self.question_id = question_id

    def answrToJson(self):
        return({'Answer Id': self.id,
                'Answer Text': self.answerText})
