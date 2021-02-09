#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 14:25:02 2021

@author: miyawaki
"""
#%%
import h5py
from box import Box
import os
import numpy
#%%
class matHandler:
    __filePath=''
    name=Box({})
    def __init__(self,filePath):
        self.__filePath=os.path.expanduser(filePath)
        with h5py.File(self.__filePath,'r') as f:
            self.name=self.__getName(f,'','');
    
    def getNum(self,path):
        with h5py.File(self.__filePath,'r') as f:
            res=f[path][()]        
            if len(res)==1:
                res=res[0]
            if len(res.T)==1:
                res=res.T[0]                
        return res
    
    def getStr(self,path):
        res=[]
        with h5py.File(self.__filePath,'r') as f:
            for col in f[path][()]:
                row=[]
                if col.dtype=='O':
                    for rIdx in range(len(col)):
                        row.append(''.join(map(chr, map(int,f[col[rIdx]][:]))))
                else:
                    for rIdx in range(len(col)):
                        row.append(''.join(map(chr, f[col[rIdx]])))

                res.append(row)
            res=numpy.array(res)
            if len(res)==1:
                res=res[0]
            if len(res.T)==1:
                res=res.T[0] 
        return res
            
    def __getName(self,h5f,keys,path):
        if keys=='':
            # print('key is empty')
            res=self.__getName(h5f,h5f.keys(),'')
            return Box(res)
        
        res={}
        for k in keys:
            # print('process ' + k)
            if k[0]=='#':
                # print('  key start with #')
                continue
            
            if isinstance(h5f[k],h5py.Dataset):
                # print('  ' + k + ' is dataset')
                res[k]=path+'/'+k
                # print(k)
                    
            elif isinstance(h5f[k],h5py.Group):
                # print('  ' + k + ' is group')
                res[k]=self.__getName(h5f[k],h5f[k].keys(),path+'/'+k)
            # else:
                # print('  ' + k + ' is something else')

        return Box(res)


