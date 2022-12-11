class Diactrics:
    def __init__(self, text):
        self.text = text

    def remove_diacritics(self):
        return self.text.replace('َِ', '').replace('َُ', '').replace('ُ', '').replace('ٍّ', 'ٌ')