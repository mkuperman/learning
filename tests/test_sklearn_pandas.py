from pandas import read_csv, DataFrame, Series
import matplotlib.pyplot as plt

def test_drivers():
    data = read_csv('Data/drivers.csv')

    # Собираем красивый графичек (и бесполезный =) )
    data.pivot_table('Koe', 'Age', 'Experience', 'count').plot(kind='bar',
                                                                    stacked = True)
    # Save in file. Not showing
    plt.savefig('driver_stacks.png')

    # зависимость опыта от возраста в две колонки
    fig, axes = plt.subplots(ncols=2)
    data.pivot_table('Koe', 'Age', 'Experience', 'count').plot(ax=axes[0],
                                                                    title='Left')
    data.pivot_table('Koe', 'Age', 'Experience', 'count').plot(ax=axes[1],
                                                                    title='Right')

    plt.savefig('experience_by_age.png')
    # Тут получилось совсем не то, что я хотел. Надо покурить мануал


    # Предварительная обработка данных
    from sklearn.preprocessing import LabelEncoder
    label = LabelEncoder()
    dicts = {}

    # задаем список значенией для кодирования
    label.fit(data.Age.drop_duplicates())
    dicts['Age'] = list(label.classes_)
    # заменяем значения из списка кодами закодированных элементов
    data.Age = label.transform(data.Age)

    # Здесь значения возраста перекодируются в цифру с вариантом. Удобно для того,
    # чтобы разбивать всех на группы
    print(data)

    data = data.drop(['Names'], axis=1)

    ## Построение моделей классификации и их анализ
    from sklearn import cross_validation, svm
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_curve, auc
    import pylab as pl

    # Определить цель
    target = data.Koe

    # Из исходных данных убираем данные о коэффициенте
    train = data.drop(['Koe'], axis=1)
    # Количество подвыборок для валидации
    kfold = 5
    # Список для записи результатов в кросс валидации разных алгоритмов
    itog_val = {}

    # Обучающая выборка
    print(train)

    # разбиваем полученные показатели на 2 подвыборки (обучающую и тестовую)
    # Параметры: Массив значений выборки, массив значений цели, соотношение, в котором будет
    # разбита обучающая выборка (в этом случае 1/4 часть ланных исходной обучающей
    # выборки выделена для тестового набора)
    # На выходе ф-я выдает 4 массива:
    # 1) Новый обучающий массив параметров
    # 2) Тестовый массив параметров
    # 3) Новый массив показателей
    # 4) Тестовоый массив показателей
    ROCtrainTRN, ROCtestTRN, ROCtrainTRG, ROCtestTRG = cross_validation.train_test_split(train, target, test_size=0.25)


    model_rfc = RandomForestClassifier(n_estimators = 70) # колво деревьев в параметре
    model_knc = KNeighborsClassifier(n_neighbors = 15) # в параметре передаем колво соседей
    model_lr = LogisticRegression(tol=0.01)
    model_svc = svm.SVC() # по умолчанию kernek = 'rbf'

    # Проверка моделей с помощью скользящего контроля
    scores = cross_validation.cross_val_score(model_rfc, train, target, cv = kfold)
    itog_val['RandomForestClassifier'] = scores.mean()
    scores = cross_validation.cross_val_score(model_knc, train, target, cv = kfold)
    itog_val['KNeighborsClassifier'] = scores.mean()
    scores = cross_validation.cross_val_score(model_lr, train, target, cv = kfold)
    itog_val['LogisticRegression'] = scores.mean()
    scores = cross_validation.cross_val_score(model_svc, train, target, cv = kfold)
    itog_val['SVC'] = scores.mean()

    DataFrame.from_dict(data = itog_val, orient='index').plot(kind='bar', legend=False)
    plt.savefig('cross_val_res.png')

test_drivers()