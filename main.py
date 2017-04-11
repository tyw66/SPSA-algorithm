# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:19:11 2017

@author: tyw66
"""
import numpy as np
from numpy  import random as rd

import matplotlib.pyplot as plt

from traits.api import HasTraits
from traits.api import Int,Str,Float
from traitsui.api import View,Item,OKCancelButtons


def testFunc(x,n):
    res=0
    for i in range(0,n):   
        res-=(x[i]-i)**2
    return res
    
##伯努利分布
def bonuli(n):
    res=np.zeros(n)
    for i in range(0,n):
        res[i]=rd.normal(0,1)
        if res[i]>0:
            res[i]=1
        else:
            res[i]=-1   

    res.shape=(1,n)##简单粗暴2333
    res_trans=np.transpose(res)
    return res_trans
    
    
def SPSA(x,func,n,iterNum,ALPHA=0.5,CK=0.02):
    print "SPSA Begin"    
    x0=x
    obj0=func(x0,n)
    obj_iter=np.zeros(iterNum)
    obj_iter.shape=(iterNum,1)
    #spsa main loop
    for curr_iter in range(0,iterNum):
        print '--',curr_iter,'--'
        alptha=ALPHA
        search_num=0
        
        #calculate gradient
        delta=bonuli(n)
        obj=func(x0+delta,n)
        objDelta=(obj-obj0)/CK
        g=objDelta*delta
        
        #gradient normalization
        gmax=np.abs(np.max(g))
        for i in range(n):
            g[i]=g[i]/gmax
            
        #update x
        x_plus=x0+alptha*g    
        obj_plus=func(x_plus,n)
        
        #line search
        while(obj_plus<obj):
            search_num=search_num+1
            if(search_num>5):
                 break
            alptha=alptha/2
            x_plus=x0+alptha*g    
            obj_plus=func(x_plus,n)
            
        #prepare the next loop    
        obj_plus=func(x_plus,n)
        if(obj_plus>obj):
            x0=x_plus
            obj0=obj_plus         
        print obj0
        obj_iter[curr_iter]=obj0
    
            
    return x_plus,obj_iter
    
class myclass(HasTraits):
    iterNum=Int(100)
    pertNum=Int(5)
    iterLen=Float(0.5)    
    pertLen=Float(0.01)
    func=Str(testFunc)
    
    View=View(
        Item('iterNum',label=u"迭代次数",tooltip="进行多少次循环"),
        Item('pertNum',label=u"扰动次数"),
        Item('iterLen',label=u"迭代步长"),
        Item('pertLen',label=u"扰动步长"),
        Item('func',label=u"待求函数"),
        title=u"优化参数设置",
        width=400,
        height=100,
        resizable=True,  
        buttons=OKCancelButtons
    )
    
    
    
if __name__=='__main__':    
    my=myclass()
    my.configure_traits()    
    u=np.array([[23],[16],[37]])

    u_opt,obj_iter=SPSA(u,my.func,3,my.iterNum,my.pertNum,my.pertLen)
    fig_obj=plt.figure(figsize=(8,4))
    
    x=np.linspace(1,my.iterNum,my.iterNum)
    plt.plot(x,obj_iter)
    fig_obj.show()
    
    