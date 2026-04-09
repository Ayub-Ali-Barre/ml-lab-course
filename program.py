import sys
import numpy as np
import pandas as pd
import matplotlib . pyplot as plt

print ( " Python version : " , sys . version )
print ( " NumPy version : " , np . __version__ )
print ( " Pandas version : " , pd . __version__ )

x = np . linspace (0 ,10 ,100)
y = np . sin ( x )

plt . plot (x , y )
plt . title ( " Test Plot " )
plt . show ()

print ( " Environment setup successful ! " )