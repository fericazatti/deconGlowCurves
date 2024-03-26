import numpy as np

# Cargar el archivo CSV
raw_data = np.loadtxt("tld_curves/raw_tld_26-02.csv", delimiter=",")


num_rows = raw_data.shape[0]
num_cols = raw_data.shape[1]

raw_data_rest = np.zeros((num_rows, num_cols // 2))

# Restar columnas consecutivas
for i in range(0, num_cols - 1, 2):
    raw_data_rest[:, i // 2] = raw_data[:, i] - raw_data[:, i+1]

np.savetxt('tld_curves/rest_raw_26-02.csv', raw_data_rest, delimiter=',')