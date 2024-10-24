import pandas as pd
from sklearn.model_selection import train_test_split

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        data = pd.read_csv(self.file_path, index_col=0)
        return data

    def split_data(self, data):
        train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
        return train_data, test_data
