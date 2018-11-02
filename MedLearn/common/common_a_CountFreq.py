#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 21:03:09 2018

@author: charleshen
"""

from MedLearn.dataset import load_MedExp
from MedLearn.utils.modelbase import ModelBase
from MedLearn.utils.pandastool import ParseDFtypes


import pandas as pd

import coloredlogs,logging
coloredlogs.install()

#import json
#import numpy as np


import os
from MedLearn.docs import getDoc
docfilename = os.path.basename(__file__).replace('.py','.md')
DOC = getDoc(docfilename)  

        
#dataset: https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/MedExp.csv
#descripion: https://rdrr.io/rforge/Ecdat/man/MedExp.html
    
class CountFreq(ModelBase):

    """频数分析方法，适用于定类（pandas dtypes: category和bool）数据，如果非定类数据，则
    根据指定的bins参数，将定量数据转化为定类数据，执行run返回的结果为一个json，其中的result是
    dataframe，具有multiindex，显示了每列中每个类别所占的百分比和每个类别出现的次数.
    
    方法
    -------
    get_info : 
        获取该模型的信息， 返回一个字典，包含‘id’和‘name’, 'description','limited'关键字
        含义分别为：模型的id, 模型的名称，模型的描述，模型的适用范围


    run:  
        参数
        ----------
        df: pandas DataFrame
            原始要分析的数据
            
        bins: int, default:10
            如果一列为数值型数据，则根据这个参数自动转化为类别型数据
            
            
        返回结果
        ----------        
            返回一个字典，带有‘result’关键字，其值为具有muti-index的pandas dataframe
    """
    
    
    
    def __init__(self, 
                 bins = 10
                 ):
        
        self.bins = bins
        self._name_ = '频数分析'

        
        
    def get_info(self):
        
        return {'id': self._id, 
                'name': self._name, 
                'description': self._description,
                'limited':''
                }


    def run(self, 
            df,
            bins = 10): 
        
        self.bins = bins
        
        
        
        msg={}
        
        numeric_cols, category_cols = ParseDFtypes(df)
        if numeric_cols != []:
            logging.warning('column %s is not category type, force convert to category by bins of %d' %(numeric_cols, self.bins) )
            msg['warning'] = '列 %s 不是定类（category）数据, 将强制通过bins:%d为转化为定类型数据' %(numeric_cols, self.bins) 
        
        res = []
        for col in df.columns:
            if col in numeric_cols:
                vc = df[col].value_counts(bins = self.bins)
                dfc = vc.to_frame(name = 'frequency')
                dfc.index = dfc.index.map(str)
                
                _sum = dfc.frequency.sum()
                dfc['percentage'] = dfc.frequency.apply(lambda x: x/_sum)
                
            else:
                vc = df[col].value_counts()
                dfc = vc.to_frame(name = 'frequency')
                _sum = dfc.frequency.sum()
                dfc['percentage'] = dfc.frequency.apply(lambda x: x/_sum).round(5)*100              
                
            index = pd.MultiIndex.from_product([[col], 
                                                dfc.index], 
                                                names=['分析项', '分析组'])
            
            dfc = dfc.set_index(index)
            
            res.append(dfc)
        
        df_res = pd.concat(res)
        
        df_res.columns = ['频数','占比(%)']
        
        return {'result':df_res, 'msg':msg}
        
        
    
            
            
            

if __name__ == '__main__':
    
    #读取数据
    df = load_MedExp()
    
    #类的初始化
    c = CountFreq()
    
    #打印该类描述的信息
    print(c.get_info().get('description'))
    
    #执行运算，传入df、bins参数, 返回一个字典
    res = c.run(df, bins = 10).get('result')
    res.to_excel('result.xlsx')
    
    
    