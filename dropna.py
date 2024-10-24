class DropNaPreprocessor:
    def __init__(self, columns):
        self.columns = columns

    def process(self, data):
        return data.dropna(subset=self.columns)
