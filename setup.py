#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 15:03:38 2018

@author: shenwanxiang
"""


import os

mypath = os.path.abspath('.')



cmd = 'echo export PYTHONPATH="\$PYTHONPATH:%s" >> ~/.bash_profile' % mypath
os.system(cmd)
os.system('source ~/.bash_profile')

cmd = 'echo export PYTHONPATH="\$PYTHONPATH:%s" >> ~/.bashrc' % mypath
os.system(cmd)
os.system('source ~/.bashrc')


'''
from setuptools import setup, find_packages
requirements=[
        'researchpy',
        'coloredlogs',
        'statsmodels',
        'factor_analyzer',
        'Markdown'
        ]


setup(name='MedLearn',
    version='0.0.2',
    description='statistics tools for medical data',
    author='shen xiaohu',
    author_email='senwanxiang@163.com',
    install_requires=requirements,
    packages=find_packages(exclude=['__pycache__'])
)
#sys.path.insert(0,mypath)
'''