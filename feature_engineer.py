from abc import ABC, abstractmethod
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer

class TransformerBase(ABC):
    def __init__(self, data, columns=None):
        self.data = data
        if columns:
            self.columns = columns
        else:
            self.columns = data.columns.tolist()

    @abstractmethod
    def transform(self):
        pass

class DataTransformer(TransformerBase):
    def __init__(self, data, columns=None):
        super().__init__(data, columns)
        self.categorical_features = [col for col in self.columns if data[col].dtype == 'object']
        self.numerical_features = [col for col in self.columns if data[col].dtype != 'object']
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('cat', OneHotEncoder(), self.categorical_features),
                ('num', 'passthrough', self.numerical_features)
            ]
        )

    def transform(self):
        transformed_data = self.preprocessor.fit_transform(self.data)
        cat_feature_names = self.preprocessor.named_transformers_['cat'].get_feature_names_out(self.categorical_features)
        all_feature_names = list(cat_feature_names) + self.numerical_features
        df_transformed = pd.DataFrame(transformed_data, columns=all_feature_names)
        
        self.data = df_transformed
        return self.data

class LabelEncoderTransformer(TransformerBase):
    def __init__(self, data, columns=None):
        super().__init__(data, columns)
        self.categorical_features = [col for col in self.columns if data[col].dtype == 'object']
        self.label_encoders = {col: LabelEncoder() for col in self.categorical_features}

    def transform(self):
        for col in self.categorical_features:
            self.data[f'{col}_encoded'] = self.label_encoders[col].fit_transform(self.data[col])
        self.data.drop(columns=self.categorical_features, inplace=True)
        return self.data

