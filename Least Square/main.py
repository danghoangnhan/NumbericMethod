# 實驗數據
# y = f(x) ，如附檔(共 n 筆數據)
# 用 Least Square ，找出 15 次到(n - 1) 次的所有多項式
# Ouput 各次數多項式的係數再由其中選擇你認為最理想的那一次多項式，將曲線繪出
import math
import os

import numpy as np
from matplotlib import pyplot as plt


def generatingData(dir):
    arr1: float = []
    arr2: float = []
    with open(os.path.dirname(os.path.realpath(__file__)) + "\\Hw4.txt") as openfileobject:
        for line in openfileobject:
            value = line.replace('\n', '')
            value = value.split()
            arr1.append(float(value[0]))
            arr2.append(float(value[1]))
    return arr1, arr2


def caculateLeastSquare(start, end, x: list, y: list):
    arr: float = []
    for i in range(start, end, 1):
        arr.append(np.poly1d(np.polyfit(x, y, i)))
    return arr


def printResult(arr: float, x: float, y: float):
    baseLine = 0
    baseValue = 1e9

    for i in range(1, 31, 1):
        for j in range(0, 45, 1):
            index = (ans[i](x[j]) - y[i])
        index = math.sqrt(index * index / (45 - i))
        if index < baseValue:
            baseValue = index
            baseLine = i
        xp = np.linspace(min(x), max(x), 100)
        plt.title("Minimum E line:" + str(baseLine + 14) + str(baseValue), fontdict=None, loc='center', pad=None)
        plt.plot(x, y, '.', xp, arr[i](xp), '-')
        plt.show()


def main():
    x, y = generatingData()
    ans: float = caculateLeastSquare(15, 44, x, y)
    printResult(ans, x, y)


main()
