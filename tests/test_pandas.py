## Import all libraries
import matplotlib.pyplot as plt
import pandas as pd
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

print('\n\n***Create data***\n\n')

# The data set will consist of 5 baby names and the
# number of births recorded for that year (1880).

# The initial set of baby names and birth rates
names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]

# merge tow lists together
BabyDataSet = list(zip(names,births))
print(BabyDataSet)

# create a DataFrame object
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print(df)

# exxport the dataframe to a .csv file
df.to_csv('baby_births.csv')

# Just separate two tables =)
print('\n\n***Get data***\n\n')

# read .csv
Locattion = r'./baby_births.csv'
df = pd.read_csv(Locattion)

print(df)

# delete temp .csv file
import os
os.remove(Locattion)

#Check data type of the columns
print('Data type of the columns:')
print(df.dtypes)


## Analyze data
print('\n\n***Analyze data***\n\n')

# To find the most popular name or the baby with the highest
# birth rate, we can do one of the following:

# Sort the dataframe and select the top row
print('Method 1:')
Sorted = df.sort_values(['Births'], ascending=False)
print(Sorted.head(1))

# Use the max() attribute to find the maximum value
print('Method 2:')
print(df['Births'].max())

print('\n\n***Present data***\n\n')

# Create graph
df['Births'].plot()

# Maximum value im the data set
MaxValue = df['Births'].max()

# Name associated with the maximum value
MaxName = df['Names'][df['Births']==df['Births'].max()].values

# Text to display on graph
Text = str(MaxValue) + ' - ' + MaxName

# Add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8,0),
             xycoords = ('axes fraction', 'data'),
             textcoords = 'offset points')

print ("The most popular name")
df[df['Births']==df['Births'].max()]

# save result in 'figure.png'
plt.savefig('figure.png')
