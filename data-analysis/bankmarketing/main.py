# Import modules
import pandas
import matplotlib.pyplot as plt
import seaborn as sns

# Get the data from dataeset
data = pandas.read_csv('bank.csv')

def z_score(data, column):
    data[f"{column}_z"] = (data[column] - data[column].mean()) / data[column].std()
    print(f"\nZ-scores for {column}:")
    print(data[[column, f"{column}_z"]].head())

    plt.figure(figsize=(10, 6))
    plt.boxplot(data[column])
    plt.title(f"{column} Box Plot")
    plt.ylabel(column)
    plt.grid()
    plt.savefig(f"results/boxplot/{column}_boxplot.png")

z_score(data, "balance")

def save_z_scores(data, column, new_column):
    data[new_column] = (data[column] - data[column].mean()) / data[column].std()
    print(f"\nZ-scores for {column} saved to {new_column}:")
    print(data[[column, new_column]].head())

save_z_scores(data, "balance", "balance_z")

def find_outliers(data, column):
    outliers = data[(data[f"{column}_z"] > 3) | (data[f"{column}_z"] < -3)]
    print(f"\nOutliers in {column}:")
    print(outliers[[column, f"{column}_z"]])

find_outliers(data, "balance")

def box_plot_outliers(data, column):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=data[column])
    plt.title(f"{column} Box Plot with Outliers")
    plt.ylabel(column)
    plt.grid()
    plt.savefig(f"results/boxplot/{column}_boxplot_outliers.png")

box_plot_outliers(data, "balance")

def replace_outliers_with_mean(data, column):
    mean = data[column].mean()
    if data[(data[f"{column}_z"] > 3) | (data[f"{column}_z"] < -3)].empty:
        print(f"\nNo outliers found in {column}.")
        return
    data.loc[(data[f"{column}_z"] > 3) | (data[f"{column}_z"] < -3), column] = mean
    print(f"\nOutliers in {column} replaced with mean:")
    print(data[[column, f"{column}_z"]].head())

replace_outliers_with_mean(data, "balance")

def remove_created_z_score_columns(data, column):
    data.drop(columns=[f"{column}_z"], inplace=True)
    print(f"\nRemoved {column}_z columns.")

remove_created_z_score_columns(data, "balance")

