import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns 
def smoke_vs_age(f):
  sns.boxplot(x='Smoking', y='Age', data=f)  #used to visualize the relation between age and smoking
  plt.title('Smoking Distribution by Age')
  plt.show()

df = pd.read_csv('thyroid_cancer_risk_data.csv')
smoke_vs_age(df)
