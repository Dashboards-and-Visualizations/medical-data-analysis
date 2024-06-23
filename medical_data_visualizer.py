'''
    This is a simple program that makes calculations and visualise medical
    examination data

    Ref: FreeCodeCamp.org - Data Analysis with Python Projects
         Project 3: Medical Data Visualizer
'''

import pandas as pd

df = pd.read_csv('medical_examination.csv')

#   determine overweight
df['height'] = df['height']/100
df['bmi'] = df['weight']/(df['height'] * df['height'])

import numpy as np
df['overweight'] = np.where(df['bmi'] > 25, '1', '0')

#   normalise data
df['cholesterol'] = np.where(df['cholesterol'] == 1, '0', '1')
df['gluc'] = np.where(df['gluc'] == 1, '0', '1')

#   convert dataset to long format
df_Long_format = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

print(df_Long_format.groupby(['cardio', 'variable', 'value']).value_counts().reset_index(name='total'))


#   plot the dataset
import matplotlib.pyplot as plt
import seaborn as sns

sns.catplot(data=df_Long_format, x='variable', hue='value', col='cardio', kind='count')
plt.tight_layout()
plt.savefig('output-figures/category-plot.jpg')
plt.show()

#   clean data
df.drop(df[(df['ap_lo'] > df['ap_hi'])].index, inplace=True)
df.drop(df[(df['height'] < df['height'].quantile(0.025))].index, inplace=True)
df.drop(df[(df['height'] > df['height'].quantile(0.0975))].index, inplace=True)
df.drop(df[(df['weight'] < df['weight'].quantile(0.025))].index, inplace=True)
df.drop(df[(df['weight'] > df['weight'].quantile(0.0975))].index, inplace=True)

#   plot correlation matrix
correlation_matrix = df.corr()
mask_matrix = np.triu(np.ones_like(correlation_matrix))
sns.heatmap(correlation_matrix, mask=mask_matrix, cmap='coolwarm', annot=True)
plt.tight_layout()
plt.savefig('output-figures/medical-data.jpg')
plt.show()

