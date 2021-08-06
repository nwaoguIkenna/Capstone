#import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
import re

# Data locations
dataPathBase = r'C:\Code\SMU\Capstone\Code\Scratch\LSTM\IAM Original'
dataImagesPath = dataPathBase + r'\lineImages-all\lineImages'
dataStrokesPath = dataPathBase + r'\lineStrokes-all\lineStrokes'
dataStrokesPath = dataPathBase + r'\original-xml-all\original'

dataTrainSet = dataPathBase + r'\task1\trainset.txt'
dataValidationSet1 = dataPathBase + r'\task1\testset_v.txt'
dataValidationSet2 = dataPathBase + r'\task1\testset_f.txt'
dataTestSet = dataPathBase + r'\task1\testset_t.txt'

dataName = r"a01-020x"
dataSub = re.findall(r'^(.+)-.+$', dataName)

print(dataSub)