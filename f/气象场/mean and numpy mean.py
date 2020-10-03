import numpy as np
import pandas as pd

dqh=pd.DataFrame({'period':[1,2,3],'name':[1,np.nan,2],'value':[1,np.nan,2]})
print(dqh['name'].mean())
print(dqh['name'].apply(np.nanmean(axis=1)))