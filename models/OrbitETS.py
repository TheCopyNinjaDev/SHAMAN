import pandas as pd
from orbit.models.dlt import ETSFull

class OrbitETS(ETSFull):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'OrbitETS'

    def fit(self, date_col, value_col):
        date_col = pd.to_numeric(date_col)
        super(OrbitETS, self).fit(date_col + value_col)

    def predict(self, pred):
        pred_df = super(OrbitETS, self).predict(pred)
        df = pd.DataFrame(pred_df['time'] + pred_df['predicion'])
        print(df.head())