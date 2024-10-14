# -*- coding: utf-8 -*-
# @Time    : 2024/9/20  12:15
# @Author  : lh
# @FileName: test.py
# @Software: PyCharm
"""
    Description:
        
"""
import pandas as pd
import numpy  as np
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.tensor([1.0])
y = np.array([1,1])
print(x,y)

