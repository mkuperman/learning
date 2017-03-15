import pandas as pd

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
age = [18, 40, 34, 22, 57]
work_start = [7, 10, 11, 8, 11]
work_end = [11, 14, 12, 17, 15]
experience = [0, 10, 3, 2, 20]
home = [[0.123123, 5.12312], [0.123123, 5.12312], [0.123123, 5.12312],
        [0.123123, 5.12312], [0.123123, 5.12312]]
work = [[6.123123, 6.12312], [6.123123, 6.12312], [6.123123, 6.12312],
        [6.123123, 6.12312], [6.123123, 6.12312]]
k = [12, 2, 4, 9, 14]

# k - тот самый коэффициент, который мы ищем

DriverDataSet = list(zip(names,age,work_start,work_end,experience,home,work,k))

df = pd.DataFrame(data = DriverDataSet, columns = ['Names', 'Age', 'Work Start',
                                                   'Work End', 'Experience',
                                                   'Home', 'Work', 'Koe'])

df.to_csv('Data/drivers.csv')
