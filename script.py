
#feito por curious0w

#importando as bibliotecas necessárias
import requests
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Definir a chave da API
api_key = "api key"

moeda = input("Coin Name" )
#raiz, obtem dados sobre a moeda
def obter_dados_historicos(api_key):
    url = f"https://www.mercadobitcoin.net/api/{moeda}/trades/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list):
            return pd.DataFrame(data)
        elif isinstance(data, dict) and 'trades' in data:
            return pd.DataFrame(data['trades'])
        else:
            print("Erro: A resposta da API não está no formato esperado.")
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter dados históricos: {e}")
        return pd.DataFrame()

def obter_preco_atual(api_key):
    url = f"https://www.mercadobitcoin.net/api/{moeda}/ticker/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return float(data['ticker']['last'])
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter preço atual: {e}")
        return None

def preparar_dados(df):
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df['price'] = df['price'].astype(float)
    X = df[['price']].values
    y = df['price'].shift(-1).dropna().values
    X = X[:-1]
    return X, y

def treinar_modelo(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def main():
    df = obter_dados_historicos(api_key)
    if not df.empty:
        X, y = preparar_dados(df)
        model = treinar_modelo(X, y)
        current_price = obter_preco_atual(api_key)
        if current_price is not None:
            future_price = model.predict(np.array([[current_price]]))
            if future_price > current_price:
                print("""💸贉- buy""")
            else:
                print("""╲┏━┳━━━━━━━━┓╲╲
╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲
╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲
╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲ -sell
╲┃◯┃╭╮╰╯┏━━━┳╯╲
╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲
╲┃╰┃◯╰┗┛┗┛╯╭┃╲╲ """)
        else:
            print("Erro: Não foi possível obter o preço atual!")
    else:
        print("Erro: Não foi possível obter dados históricos da moeda Marinade!")

if __name__ == "__main__":
    main()
