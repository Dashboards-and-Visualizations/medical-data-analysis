"""
This is a simple program that makes calculations and visualizes medical examination data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading the data: {e}")

def process_data(df):
    try:
        df['height'] = df['height'] / 100
        df['bmi'] = df['weight'] / (df['height'] ** 2)
        df['overweight'] = np.where(df['bmi'] > 25, 1, 0)
        df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
        df['gluc'] = np.where(df['gluc'] == 1, 0, 1)
        return df
    except KeyError as e:
        raise KeyError(f"Missing expected column: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while processing the data: {e}")

def convert_to_long_format(df):
    try:
        df_long = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
        return df_long
    except KeyError as e:
        raise KeyError(f"Missing expected column for melting: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while converting to long format: {e}")

def plot_category_data(df_long, output_path):
    try:
        sns.catplot(data=df_long, x='variable', hue='value', col='cardio', kind='count')
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
    except Exception as e:
        raise RuntimeError(f"An error occurred while plotting category data: {e}")

def clean_data(df):
    try:
        df = df[df['ap_lo'] <= df['ap_hi']]
        df = df[df['height'] >= df['height'].quantile(0.025)]
        df = df[df['height'] <= df['height'].quantile(0.975)]
        df = df[df['weight'] >= df['weight'].quantile(0.025)]
        df = df[df['weight'] <= df['weight'].quantile(0.975)]
        return df
    except KeyError as e:
        raise KeyError(f"Missing expected column for cleaning: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while cleaning the data: {e}")

def plot_correlation_matrix(df, output_path):
    try:
        correlation_matrix = df.corr()
        mask_matrix = np.triu(np.ones_like(correlation_matrix, dtype=bool))
        sns.heatmap(correlation_matrix, mask=mask_matrix, cmap='coolwarm', annot=True)
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
    except Exception as e:
        raise RuntimeError(f"An error occurred while plotting the correlation matrix: {e}")

def main():
    try:
        df = load_data('../data/medical_examination.csv')
        df = process_data(df)
        df_long = convert_to_long_format(df)
        plot_category_data(df_long, '../figures/category-plot.jpg')
        df_cleaned = clean_data(df)
        plot_correlation_matrix(df_cleaned, '../figures/medical-data.jpg')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
