import pandas as pd
import matplotlib.pyplot as plt

FILES = ['test/general.csv',
         'test/prenatal.csv',
         'test/sports.csv']

data_frames = []
for file in FILES:
    data_frames.append(pd.read_csv(file))
    data_frames[-1].columns = data_frames[0].columns

data = (pd.concat(data_frames, ignore_index=True).
        drop('Unnamed: 0', axis='columns'))
data = data.dropna(thresh=1)
data.loc[(data.gender == 'man') |
         (data.gender == 'male'), 'gender'] = 'm'
data.loc[(data.gender == 'woman') |
         (data.gender == 'female') |
         (data.hospital == 'prenatal'), 'gender'] = 'f'
zero_cols = ['bmi', 'diagnosis', 'blood_test',
             'ecg', 'ultrasound', 'mri',
             'xray', 'children', 'months']
data[zero_cols] = data[zero_cols].fillna(0)

# 1. What is the most common age of a patient among all hospitals?
# Plot a histogram and choose one of the following age ranges:
# 0-15, 15-35, 35-55, 55-70, or 70-80.
data.age.plot(kind='hist', bins=[0, 15, 35, 55, 70, 80])
plt.show()
plt.clf()
ans = ['15-35']

# 2. What is the most common diagnosis among patients in all hospitals?
# Create a pie chart.
data.diagnosis.value_counts().plot(kind='pie')
plt.show()
plt.clf()
ans.append(f'{data.diagnosis.mode()[0]}')

# 3. Build a violin plot of height distribution by hospitals.
# What is the main reason for the gap in values? Why there are two peaks,
# which correspond to the relatively small and big values?
plt.violinplot(data.height)
plt.show()
plt.clf()
ans.append("Sports hospital uses feets and other hospitals use meters")

# output
question_n = ['1st', '2nd', '3rd']
for number, answer in zip(question_n, ans):
    print(f'The answer to the {number} question: {answer}')
