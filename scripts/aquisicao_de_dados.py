import os
import pandas as pd

def validar_estrutura():
    caminhos_possiveis = [
        'data/alzheimers_disease_data.csv',
        '../data/alzheimers_disease_data.csv',
        '../../data/alzheimers_disease_data.csv',
        './alzheimers_disease_data.csv'
    ]
    
    caminho_final = None
    for cp in caminhos_possiveis:
        if os.path.exists(cp):
            caminho_final = cp
            break
            
    if caminho_final:
        df = pd.read_csv(caminho_final)
        colunas = len(df.columns)
        linhas = len(df)
        
        
    print(df)

    print(f"base encontrada em: {caminho_final}")
    print(f"colunas: {colunas}")
    print(f"linhas: {linhas}")
        

    if colunas == 35 and linhas >= 2148:
            print("deu certo")
    else:
            print("conflito")
    
  

if __name__ == "__main__":
    validar_estrutura()