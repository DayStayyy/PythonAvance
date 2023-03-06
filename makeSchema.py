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

makeMeanTemp(df)