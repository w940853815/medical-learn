#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 17:26:43 2018

@author: charleshen
"""
class ModelBase(object):
    '''base class, has basic attributes of _id, _name, _description, _limitation'''

    def __init__(self, model_id = None, model_limiation = None):
        self._id_ = model_id
        self._limitation_ = model_limiation
        
        
    @property
    def _name(self):
        return self._name_
    
    
    @_name.setter
    def _name(self, _name):
        self._name_ = _name   
    
    @property
    def _id(self):  
        return self.__class__.__name__

    @property
    def _description(self):
        return self.__doc__    
    
    @property
    def _limitation(self):
        return self._limitation_

    @_limitation.setter
    def _limitation(self, limitation):
        self._limitation_ = limitation
        
        
  
    



