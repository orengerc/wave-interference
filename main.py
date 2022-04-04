"""
Runs analysis according to specific demands
"""

from DataHandler import *
from Graph import *
from CurveFit import *
from Equations import *
from PIL import Image
from ImageHandler import *
import numpy as np
from scipy.stats import linregress
import os
import matplotlib.pyplot as plt
import csv
import pandas as pd


def parse_txt_to_dataframe(path):
    df = pd.DataFrame()
    with open(path) as tsv:
        for i, line in enumerate(csv.reader(tsv, delimiter="\t")):
            if i > 7:
                df = df.append([line])
    return df


def graph_interference_pattern(df):
    print(df)
    print(type(df[3]), df[3].shape())
    # plt.plot(df[3], df[2])
    # plt.show()


def write_df_to_csv(df, name):
    print("to csv")
    df.to_csv(os.path.join(folder, name) + '.csv')


if __name__ == '__main__':
    correction_data = parse_txt_to_dataframe(
        "C:/Users/ORENGER/Desktop/orens_stuff/wave-interference/data/week2/correction.txt")
    correction_data.to_csv("data/week2/correction_data.csv")

    for n_slits in ["1_slit", "2_slits"]:
        folder = "data\\week2\\{0}".format(n_slits)
        print(folder)
        for filename in os.listdir(folder):
            print(filename)
            data_frame = parse_txt_to_dataframe(os.path.join(folder, filename))
            write_df_to_csv(data_frame, os.path.splitext(filename)[0])
            graph_interference_pattern(data_frame)
