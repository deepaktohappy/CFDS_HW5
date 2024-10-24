class FillNaPreprocessor:
    def __init__(self, columns):
        self.columns = columns

    def process(self, data):
        for column in self.columns:
            data[column].fillna(data[column].mean(), inplace=True)
        return data
