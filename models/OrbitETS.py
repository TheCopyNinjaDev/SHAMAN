import pandas as pd
from orbit.models.dlt import ETSFull


class OrbitETS(ETSFull):

    def __init__(self, date_col, response_col, **kwargs):
        super().__init__(date_col=date_col, response_col=response_col, **kwargs)
        self.name = 'OrbitETS'

    def fit(self, train):
        train[self.date_col] = pd.to_numeric(train[self.date_col])
        super(OrbitETS, self).fit(df=train)

    def predict(self, test, **kwargs):
        test[self.date_col] = pd.to_numeric(test[self.date_col])
        prediction = super(OrbitETS, self).predict(test)
        prediction[self.date_col] = pd.to_datetime(prediction[self.date_col])
        prediction = prediction[['time', 'prediction']]
        return prediction
