#!/usr/bin/python
# -*- coding:utf-8 -*-


'''from data import Data'''
import numpy as np
import math


class Data(object):

    def __init__(self):
        self.data = []
        self.name = input('输入数据名：')
        self.n = -1

    def addData(self):
        self.data.clear()#清空保证append正常运行
        self.n = int(input('输入数据个数: '))
        for i in range(self.n):
            print('请输入第%d个数据' % (i + 1))
            self.data.append( float(input()) )
        self.showdata()

    def showdata(self):
        print('一共%d个数据'%(self.n))
        print(self.data)

    def showAll(self):
        self.showdata()
        print('平均：'+str(self.average()))
        self.A_difference()


    def average(self):
        return sum(self.data)/self.n

    def A_difference(self):
        ave = self.average()
        A = math.sqrt(sum(list(map(lambda x:(x - ave)**2,self.data))) /(self.n*(self.n-1)))
        print('A类不确定度是：%lf'%(A))
        print('A相对不确定度是：%lf %%'%(A/ave*100))
        return A

def analyseData():
    data = Data()
    while (True):
        print('1：输入，2：显示结果，0：退出')
        key = int(input())
        if (key == 1):
            data.addData()
        elif (key == 2):
            data.showAll()
        elif (key == 0):
            break

if __name__ =='__main__':
    analyseData()
