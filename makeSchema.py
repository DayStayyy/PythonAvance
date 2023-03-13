import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("merged_data.csv")
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')


def makeMeanTemp(df):
    mean_temp_by_year = df.groupby(df['date'].dt.year)['t'].mean().reset_index()
    mean_temp_by_year.rename(columns={'t': 'TMean'}, inplace=True)
    xpoints = mean_temp_by_year.date
    ypoints = mean_temp_by_year.TMean
    plt.plot(xpoints, ypoints)
    plt.xlabel("year")
    plt.ylabel("temp mean")
    plt.legend(["temp mean","year"])
    plt.savefig("mean_temp.png")


def makeEolienne(df):
    df['dd'] = pd.to_numeric(df['dd'], errors='coerce')
    df['eoliene_can_run'] = (df['dd'] > 4.16667) & (df['dd'] < 25)
    # Count the number of True and False values in the 'is_valid' column
    value_counts = df['eoliene_can_run'].value_counts()
    # Plot a pie chart of the value counts
    plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%')
    plt.title('% of days eoliene can run')
    plt.savefig("eoliene_can_run.png")



makeEolienne(df)

