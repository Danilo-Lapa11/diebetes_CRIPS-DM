import pandas as pd
from scipy.io import arff

# Carregar o arquivo ARFF
data, meta = arff.loadarff('data/phpvqZpLa.arff')

# Converter para DataFrame
df = pd.DataFrame(data)

# Converter colunas de bytes para string
for col in df.select_dtypes([object]):  # Seleciona colunas do tipo objeto (possíveis bytes)
    df[col] = df[col].str.decode('utf-8')

# Salvar como CSV
df.to_csv("diabetes.csv", index=False)
