import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

# x = [29.0, 39.0, 45.2, 53.3, 59.1, 63.5, 71.9]
# y = [40, 60, 80, 100, 120, 140, 160]

# distance 80
# x = [0.26, 0.32, 0.38, 0.45, 0.50, 0.56, 0.63, 0.71, 0.75]
# y = [190, 185, 180, 175, 170, 165, 160, 155, 150]

# distance 40
# x = [0.22, 0.33, 0.47, 0.53, 0.65]
# y = [180, 175, 170, 165, 160]


def draw_line(x, y, column):
    plt.rcParams['figure.figsize'] = (12.0, 9.0)
    plt.title(column)
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    num = 0
    den = 0
    for i in range(len(x)):
        num += (x[i] - x_mean) * (y[i] - y_mean)
        den += (x[i] - x_mean) ** 2
    m = num / den
    c = y_mean - m * x_mean

    print(m, c)

    y_pred = m * x + c
    plt.scatter(x, y)
    plt.plot([min(x), max(x)], [max(y_pred), min(y_pred)], color='red')
    plt.show()


def reverse(lst):
    return [ele for ele in reversed(lst)]


def read_data(column, file='height_data.csv'):
    df = pd.read_csv(file)
    print(df)
    x = df[column].tolist()
    x = reverse(x)
    y = [190, 185, 180, 175, 170, 165, 160, 155, 150]
    return x, y


def read_csv(file='height_data.csv'):
    df = pd.read_csv(file)
    print(df)
    return df


def clean_data(df):
    df.drop('40', axis=1, inplace=True)
    distance_lst = range(60, 200, 20)
    x, y, z = [], [], []
    for index, row in df.iterrows():
        height = row[0]
        row = row[1:]
        for idx, distance in enumerate(distance_lst):
            x.append(row[idx])
            y.append(distance)
            z.append(height)
    return x, y, z


def draw(z):
    x = np.linspace(60, 180, 7)
    y = np.linspace(150, 190, 9)
    x, y = np.meshgrid(x, y)
    print(x)
    print(y)
    ax = plt.axes(projection='3d')
    ax.plot_surface(y, x, z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_title('surface')
    plt.show()


def write_data(x, y, z):
    fields = ['s', 'd', 'h']
    rows = zip(x, y, z)

    with open('3d_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        for row in rows:
            writer.writerow(row)
        # write.writerows(rows)


if __name__ == '__main__':
    df = read_csv()
    x, y, z = clean_data(df)
    write_data(x, y, z)
    # z = np.array(x, dtype=float)
    # z = z.reshape(9, 7)
    # print(z)
    # draw(z)















    # fit_curve()

    # df = read_csv()
    # z, y, x = clean_data(df)
    # draw_3d(x, y, z)
    # print(x)
    # print(y)
    # print(z)


    # draw_3d()
    # column = '180'
    # x, y = read_data(column)
    # draw_line(x, y, column)
