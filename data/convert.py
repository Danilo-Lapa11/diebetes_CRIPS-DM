import pandas as pd
from scipy.io import arff

# Carregar o arquivo ARFF
data, meta = arff.loadarff("data/phpvqZpLa.arff")

# Converter para DataFrame
df = pd.DataFrame(data)

# Salvar como CSV
df.to_csv("diabetes.csv", index=False)
