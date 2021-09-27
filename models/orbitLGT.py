import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('seaborn')
from orbit.models.lgt import LGTFull


class OrbitDLT(LGTFull):

    def __init__(self, date_col, response_col, **kwargs):
        super().__init__(date_col=date_col, response_col=response_col, **kwargs)
        self.name = 'LGTFull'
        self.__prediction = None
        self.__test = None

    def fit(self, train):
        new_train = train.copy()
        new_train[self.date_col] = pd.to_numeric(new_train[self.date_col])

        super(LGTFull, self).fit(df=new_train)

    def predict(self, test, **kwargs):
        new_test = test.copy()
        new_test[self.date_col] = pd.to_numeric(new_test[self.date_col])

        prediction = super(LGTFull, self).predict(new_test)

        prediction[self.date_col] = pd.to_datetime(prediction[self.date_col])
        prediction = prediction[['time', 'prediction']]
        prediction.columns = ['time', 'price']

        self.__prediction = prediction
        self.__test = test

        return prediction

    def show(self):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(self.__test['time'], self.__test['price'], c='b', label="real")
        ax.plot(self.__test['time'], self.__prediction['price'], c='r', label="prediction")
        plt.legend()
        plt.show()
