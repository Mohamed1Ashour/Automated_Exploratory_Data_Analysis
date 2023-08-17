# Data Analyzer Tool

Data Analyzer Tool is a Python script that provides a comprehensive set of functions to analyze and visualize data from various sources such as CSV and Excel files. With this tool, you can quickly gain insights into your dataset, perform statistical analysis, identify outliers, handle missing values, and generate various types of plots and visualizations..
.

## Features:

- Load data from both CSV and Excel files.
- Perform descriptive data analysis, statistics, and visualization tasks.
- Identify columns with missing values and outliers.
- Handle missing values through removal or imputation.
- Remove outliers based on interquartile range.
- Generate a range of plots, including histograms, KDE plots, ECDF plots, regression plots, and more.

# Getting Started:

## Prerequisites:

Make sure you have the required libraries installed by running:

pip install pandas numpy matplotlib seaborn keyboard

## Usage:

1. Clone this repository to your local machine.

2. Open a terminal or command prompt and navigate to the cloned directory.

3. Run the script by executing:

python data_analyzer.py

4. Follow the prompts to load your data file and explore the available analysis and visualization options.

## How It Works:

The Data Analyzer Tool script is structured as follows:

- Import necessary libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Keyboard.
- Define a DataAnalyzer class that encapsulates data loading, analysis, and visualization methods.
- Instantiate the class, load the data, and provide an interactive menu for users to choose analysis functions.
- The tool provides various descriptive statistics, correlation matrices, outlier detection, and visualization functions.

## Customization and Contribution:

The script is designed to be extensible. You can:

- Add new analysis functions to the DataAnalyzer class.
- Modify existing functions to fit specific requirements.
- Enhance the tool's functionality and visualization capabilities.

Feel free to contribute to the project by submitting pull requests or reporting issues.

## Acknowledgements:

The Data Analyzer Tool is inspired by the need for a streamlined data analysis process. It leverages the power of popular Python libraries to provide users with insightful insights into their datasets.
