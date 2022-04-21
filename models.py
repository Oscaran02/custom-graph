from datetime import datetime
from time import sleep

import pandas
import warnings
warnings.simplefilter("ignore")


class report:
    def __init__(self, start_date, end_date, country):
        self.df = None

        # Dates are set as date format if they have something different from 0
        if str(start_date) == "0" or str(end_date) == "0":
            self.start_date = str(start_date)
            self.end_date = str(end_date)
        else:
            self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
            self.end_date = datetime.strptime(end_date, "%d/%m/%Y")

        self.country = country

    # Method to get the data from Excel file and return a dataframe
    def get_data_from_excel(self):
        self.df = pandas.read_excel("uploads/data.xlsx",
                                    header=0,
                                    parse_dates=['Fecha ingreso'],
                                    decimal=",",
                                    engine="openpyxl",
                                    )

    # Groups the data grouped by country
    def group_by_country(self):
        self.df = self.df[self.df["País"] == self.country]

    # returns dataframe with the data grouped by dates given in the parameter
    def group_by_dates(self):
        # If one of the dates is 0, it means that the user didn't select a date, so we will use the entire dataframe
        if self.start_date == "0" or self.end_date == "0":
            pass
        else:
            self.df = self.df[self.start_date <= self.df["Fecha ingreso"]]
            self.df = self.df[self.end_date >= self.df["Fecha ingreso"]]

    # Filters the dataframe
    def filter_data(self):
        self.group_by_country()
        self.group_by_dates()

    # Returns the average times in the warehouse - data1
    def average_times_in_warehouse(self):
        return self.df.mean(axis=0, skipna=True, numeric_only=True)[
            ["Tiempo para foto", "Delta foto-registro datos", "Delta registro datos-ubicación bodega",
             "Delta ubicación bodega-tránsito"]]

    # Returns the states of the packages - data2
    def state_of_package(self):
        return self.df["Estado"].value_counts()

    # Returns the states of the packages in transit - data3
    def state_of_package_in_transit(self):
        return self.df["Estado Tránsito"].value_counts()

    # Returns the pre-alerts - data4
    def prealerts(self):
        return self.df["Prealerta"].value_counts()

    # Returns the origin of the packages - data5
    def origin_of_package(self):
        return self.df["Origen"].value_counts()

    # Returns the international courier - data6
    def international_courier(self):
        return self.df["Courier \ninternacional"].value_counts()

    # Returns the alliance of the packages - data7
    def alliance_of_package(self):
        return self.df["Alianza"].value_counts()

    # Returns the local courier - data8
    def local_courier(self):
        return self.df["Courier local"].value_counts()

    # Returns the department of the customer - data9
    def department_of_customer(self):
        return self.df["Departamento"].value_counts()

    # Returns the average times in routes - data10
    def average_time_in_routes(self):
        return self.df.mean(axis=0, skipna=True, numeric_only=True)[
            ["Tiempo en bodega", "Tiempo tránsito", "Delta aduana-entrega \n (# Dias hábiles)",
             "Tiempo entrega \n(# Dias hábiles)"]]

    def set_data(self):
        print("Setting data...")
        self.get_data_from_excel()
        sleep(5)
        print("Data set")
        self.filter_data()
