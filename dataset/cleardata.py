import os
import numpy as np


def iris():
    iris_name = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    data = [];
    indir = os.path.abspath('../dataset/iris')

    row = 0
    for line in open(os.path.join(indir, 'iris.data')):
        src = line.split(',')
        data.extend([float(num) for num in src[:-1]])
        data.append(iris_name[src[-1].strip()])
        row += 1
    data = np.array(data).reshape(row, 5)
    return data


def wine():
    data = [];
    indir = os.path.abspath('../dataset/wine')
    row = 0
    for line in open(os.path.join(indir, 'wine.data')):
        src = line.split(',')
        data.extend([float(num) for num in src])
        row += 1
    data = np.array(data).reshape(row, 14)
    return data

def car():

    label = {'vhigh': 0, 'high' : 1, 'med' : 2, 'low' : 3}
    lug_label = {'small': 0, 'med': 1, 'big':2}
    car_dic = {'buying' : label, 'maint' : label, 'lug_boot': lug_label, 'safety': label}
    result_label = {'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}

    data = [];
    indir = os.path.abspath('../dataset/car')
    row = 0
    for line in open(os.path.join(indir, 'car.data')):
        src = line.split(',')
        buying = car_dic['buying'][src[0]]
        maint = car_dic['maint'][src[1]]
        try:
            doors = int(src[2])
        except ValueError:
            doors = 5

        try:
            persons = int(src[3])
        except ValueError:
            persons = 6

        lug_boot = car_dic['lug_boot'][src[4]]
        safety = car_dic['safety'][src[5]]
        result = result_label[src[6].strip()]

        data.extend([buying, maint, doors, persons, lug_boot, safety, result])

        row += 1
    data = np.array(data).reshape(row, 7)
    return data

def adult():
    return [1,2,2,2,2,4]
