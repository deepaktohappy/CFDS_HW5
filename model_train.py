from sklearn.ensemble import RandomForestClassifier

class Model:
    def __init__(self, model=RandomForestClassifier, model_params=None):
        self.model_class = model
        self.model_params = model_params if model_params else {}
        self.model = self.model_class(**self.model_params)
    
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict_proba(X_test)
