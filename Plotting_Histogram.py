import pandas as pd 
from matplotlib import pyplot as plt
whole_data = pd.read_csv("yourFileDirerctory/weatherHistory.csv")
temp_data = whole_data['Temperature (C)']
#temp_data_ = temp_data.to_numpy()
plt.hist(temp_data)
plt.show()
