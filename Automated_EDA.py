import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import keyboard


class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.load_data()

    def load_data(self):
        if self.file_path.endswith('.csv'):
            self.df = pd.read_csv(self.file_path)

        elif (self.file_path.endswith('.xls')) or (self.file_path.endswith('.xlsx')):
            self.df = pd.read_excel(self.file_path)

        self.categorical_data = self.df.select_dtypes(
            include=['object']).columns
        self.numerical_data = self.df.select_dtypes(
            include=['int', 'float']).columns

    def data_description(self):
        print("Data Overview:")
        print(self.df.head(5))
        print('-' * 50)
        print('\n')

        print("Data Types Overview:")
        print(self.df.dtypes)
        print("-" * 50)
        print('\n')

        print('Columns Names')
        print(self.df.columns)
        print('-' * 50)
        print('\n')

        print("Columns with Missing Values:")
        print(self.df.isna().sum())
        print("-" * 50)
        print('\n')

        for col in self.categorical_data:
            print(f"'{col}':")
            print("Number of Unique Categories:", self.df[col].nunique())
            print("Percentage of Missing Values:",
                  (self.df[col].isna().sum()/len(self.df)) * 100)
            print('\n')

    def statistics(self):

        print("Correlation")
        print(self.df.corr())
        print("-" * 50)
        print('\n')

        for col in self.df.select_dtypes(include=np.number).corr():
            print(f"Column: {col}")
            print(
                f"Coefficient of Variation =  {(self.df[col].std() / self.df[col].mean()) * 100:.2f}")
            print("-" * 50)
            print('\n')

        for col in self.numerical_data:
            print(f"Descriptive Statistics for '{col}':")
            print(self.df[col].describe())
            print('\n')

            print(f"Skewness: {self.df[col].skew()}")
            print(f"Kurtosis: {self.df[col].kurt()}")
            print("-" * 50)
            print('\n')

    def percentage_of_outliers_in_columns(self):
        outlier_percentages = {}

        for col in self.numerical_data:
            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5*iqr
            upper_bound = q3 - 1.5*iqr
            outliers = self.df[(self.df[col] < lower_bound)
                               | (self.df[col] > upper_bound)]
            outlier_percentage = (len(outliers) / len(self.df)) * 100
            outlier_percentages[col] = outlier_percentage

        for key, value in outlier_percentages.items():
            print("\n")
            print(f"{key} ==> {value}")
            print("-" * 50)

    def handling_missing_values(self):
        for col in self.numerical_data:
            missing_percentage = (
                self.df[col].isna().sum() / len(self.df)) * 100
            if missing_percentage <= 5.0:
                self.df.dropna(subset=[col], inplace=True)
            else:
                self.df[col].fillna(self.df[col].median(), inplace=True)
        print("-" * 50)
        print("Your Data After Handling Missing Values ==> ")
        print("-" * 50)
        self.data_description()
        print("-" * 50)
        self.statistics()

    def remove_outliers(self):
        for col in self.numerical_data:
            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5*iqr
            upper_bound = q3 - 1.5*iqr
            self.df = self.df[(self.df[col] >= lower_bound)
                              & (self.df[col] <= upper_bound)]
        print("-" * 50)
        print("Your Data After Handling Missing Values ==> ")
        print("-" * 50)
        self.data_description()
        print("-" * 50)
        self.statistics()

    def plot_histograms_plots(self, x):
        sns.histplot(self.df[x], kde=True)
        plt.title(f'Histogram of {x}')
        plt.xlabel(x)
        plt.ylabel('Frequency')
        plt.show()

    def plot_kde_plots(self, x):
        sns.kdeplot(self.df[x], shade=True)
        plt.title(f'KDE Plot of {x}')
        plt.xlabel(x)
        plt.ylabel('Density')
        plt.show()

    def plot_ecdf_plots(self, x):
        sns.ecdfplot(data=self.df, x=x)
        plt.title(f'ECDF Plot of {x}')
        plt.xlabel(x)
        plt.ylabel('Cumulative Probability')
        plt.show()

    def plot_regplots(self, x, y):
        sns.regplot(data=self.df, x=x, y=y)
        plt.title(f'Regression Plot of {x} vs {y}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

    def plot_pair_plots(self):
        sns.pairplot(self.df[self.numerical_data])
        plt.title('Pair Plot of Numerical Columns')
        plt.show()

    def plot_scatter_plots(self, x, y):
        sns.scatterplot(data=self.df, x=x, y=y)
        plt.title(f'Scatter Plot of {x} vs {y}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

    def plot_line_plots(self, x, y):
        sns.lineplot(data=self.df, x=x, y=y)
        plt.title(f'Line Plot of {x} vs {y}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

    def plot_box_plots(self, x):
        sns.boxplot(data=self.df, y=x)
        plt.title(f'Box Plot of {x}')
        plt.ylabel(x)
        plt.show()

    def plot_count_plots(self, x):
        sns.countplot(data=self.df, x=x)
        plt.title(f'Count Plot of {x}')
        plt.xlabel(x)
        plt.ylabel('Count')
        plt.xticks(rotation=90)
        plt.show()

    def plot_bar_plots(self, x, y):
        sns.barplot(data=self.df, x=x, y=y)
        plt.title(f'Bar Plot of {x}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.xticks(rotation=90)
        plt.show()

    def plot_point_plots(self, x, y):
        sns.pointplot(data=self.df, x=x, y=y)
        plt.title(f'Point Plot of {x}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.xticks(rotation=90)
        plt.show()

    def run_selected_function(self):

        function_mapping = {
            '1': self.data_description,
            '2': self.statistics,
            '3': self.percentage_of_outliers_in_columns,
            '4': self.handling_missing_values,
            '5': self.remove_outliers,
            'h': self.plot_histograms_plots,
            'k': self.plot_kde_plots,
            'e': self.plot_ecdf_plots,
            'r': self.plot_regplots,
            'a': self.plot_pair_plots,
            's': self.plot_scatter_plots,
            'l': self.plot_line_plots,
            'b': self.plot_box_plots,
            'c': self.plot_count_plots,
            'm': self.plot_bar_plots,
            'p': self.plot_point_plots,
            '0': exit}

        while True:
            print("Press the key corresponding to the function you want to run:")
            print("-" * 50)
            print("\n")
            print("1 - Data Description (Data Overview, Data Types Overview, Columns Names, Columns with Missing Values, Number of Unique Categories, Percentage of Missing Values)")
            print("2 - Statistics (Correlation, Coefficient of Variation, Descriptive Statistics, Skewness, Kurtosis)")
            print("3 - Percentage of Outliers in Columns")
            print("4 - Handling Missing Values remove or fill")
            print("5 - Remove Outliers")
            print("h - Plot Histograms")
            print("k - Plot KDE plots")
            print("e - Plot ECDF plots")
            print("r - Plot Regression plots *")
            print("a - Plot pair plots")
            print("s - Plot scatter plots *")
            print("l - Plot line plots *")
            print("b - Plot box plots")
            print("c - Plot count plots")
            print("m - Plot bar plots *")
            print("p - Plot point plots *")
            print("0 - Quit")
            print("*" * 70)
            try:
                key = keyboard.read_event(suppress=True).name
                if key == '0':
                    print("Quitting...")
                    break
                if key in ['1', '2', '3', '4', '5', 'a']:
                    function_mapping[key]()
                elif key in ['h', 'k', 'e', 'b']:
                    print(
                        f"Available numerical columns: {list(self.numerical_data)}")
                    x = input(
                        "Enter the numerical column name for selected plot: ")
                    if x in self.numerical_data:
                        function_mapping[key](x)
                    else:
                        print("+" * 50)
                        print("Invalid numerical column name.")
                    continue

                elif key in ['r', 's', 'l', ]:
                    print(
                        f"Available numerical columns: {list(self.numerical_data)}")
                    x_col = input(
                        "Enter the numerical column name for x-axis: ")
                    y_col = input(
                        "Enter the numerical column name for y-axis: ")
                    if (x_col in self.numerical_data) and (y_col in self.numerical_data):
                        function_mapping[key](x_col, y_col)
                    else:
                        print("+" * 50)
                        print("Invalid numerical column name")

                elif key in ['m', 'p']:
                    print(
                        f"Available categorical columns: {list(self.categorical_data)}")
                    print(
                        f"Available numerical columns: {list(self.numerical_data)}")
                    x_col = input(
                        "Enter the categorical column name for x-axis: ")
                    y_col = input(
                        "Enter the numerical column name for y-axis: ")
                    if (x_col in self.categorical_data) and (y_col in self.numerical_data):
                        function_mapping[key](x_col, y_col)
                    else:
                        print("+" * 50)
                        print(
                            "Invalid column names. x should be categorical and y should be numerical")

                elif key == 'c':
                    print(
                        f"Available categorical columns: {list(self.categorical_data)}")
                    x = input(
                        "Enter the categorical column name for selected plot: ")
                    if x in self.categorical_data:
                        function_mapping[key](x)
                    else:
                        print("+" * 50)
                        print("Invalid categorical column name")
                else:
                    print('=' * 50)
                    print("Invalid key. Press a valid key to run a function.")
                    print('=' * 50)

            except KeyboardInterrupt:
                print("\nInterrupted by user. Exiting...")
                break
            except Exception as e:
                print(f"An error occurred: {e}")


def main():
    file = input('Add your File Path: ')
    file_path = os.path.join(file)
    print("\n")

    try:
        analyzer = DataAnalyzer(file_path)
        analyzer.run_selected_function()
    except:
        print("File not found. Enter the correct path.")


if __name__ == "__main__":
    main()
