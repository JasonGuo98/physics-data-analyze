#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test moudle'

__author__ = 'Jason Guo'

import math
PI = 3.14159265358979


class DEG(object):

    def __init__(self,name):
        self.name =str(name)
        self.rad = 0

    def __add__(self,other):
        ans = DEG('ans')
        ans.rad = self.rad + other.rad
        # ans.deg= [self.deg[i]+other.deg[i] for i in range(3)]
        # for i in range(2):
        #     if(ans.deg[2-i]>=60):
        #         ans.deg[1-i]+=1
        #         ans.deg[2-i]-=60
        return ans

    def set(self,mod ='DEG'):
        times = 60
        half_full = 180
        du = 0
        fen = 1
        miao = 2
        deg=[0,0,0]
        if (mod == 'DEG'):
            print('角度模式\n请输入角度：')
            deg[du]=int(input('输入度：'))
            deg[fen] = int(input('输入分：'))
            deg[miao] = int(input('输入秒：'))
            self.rad = (deg[miao] + deg[fen]*times+deg[du]*times*times)/(half_full*times*times)*PI
        elif(mod == 'RAD'):
            print('弧度模式\n请输入弧度：')
            self.rad = float(input('输入弧度：'))

        self.print()

    def print(self):
        print('name = '+ self.name)
        print('rad = %f'%self.rad)

    def __mul__(self,num):
        ans = DEG('ans')
        ans.rad = self.rad * num
        return ans











