# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:19:11 2017

@author: tyw66
"""
import numpy as np
from numpy  import random as rd


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
    
    
    
if __name__=='__main__':
    u=np.array([[23],[16],[37]])
    u_opt,obj_iter=SPSA(u,testFunc,3,500,0.5,0.02)

    