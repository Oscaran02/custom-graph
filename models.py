from datetime import datetime
from time import sleep

import pandas
import warnings
warnings.simplefilter("ignore")


class report:
    def __init__(self):
        self.df = None

    # Method to get the data from Excel file and return a dataframe
    def get_data_from_excel(self):
        self.df = pandas.read_excel("uploads/data.xlsx",
                                    header=0,
                                    decimal=",",
                                    engine="openpyxl",
                                    )

    # Returns the average times in the warehouse - data1
    def average_times(self):
        return self.df.mean(axis=0, skipna=True, numeric_only=True)

    def set_data(self):
        print("Setting data...")
        self.get_data_from_excel()
        sleep(5)
        print("Data set")
