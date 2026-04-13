import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid")

def carregar():
    f = 'data/alzheimers_disease_data.csv'
    if not os.path.exists(f): f = '../data/alzheimers_disease_data.csv'
    d = pd.read_csv(f)
    
    d['Gender'] = d['Gender'].map({0: 'Masculino', 1: 'Feminino'})
    d['Ethnicity'] = d['Ethnicity'].map({0: 'Caucasiano', 1: 'Afrodescendente', 2: 'Asiatico', 3: 'Outro'})
    d['EducationLevel'] = d['EducationLevel'].map({0: 'Nenhum', 1: 'Ensino Medio', 2: 'Graduacao', 3: 'Pos-Graduacao'})
    d['Alzheimer'] = d['Diagnosis'].map({0: 'Nao', 1: 'Sim'})
    
    return d

def grafico_genero(d):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=d, x='Gender', hue='Alzheimer')
    plt.title(' Alzheimer por Genero')
    plt.xlabel('Sexo')
    plt.ylabel('Pacientes')
    plt.show()

def grafico_etnia(d):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=d, x='Ethnicity', hue='Alzheimer')
    plt.title('Proporção de Etnia dos Pacientes')
    plt.xlabel('Etnia')
    plt.ylabel('Contagem')
    plt.show()

def grafico_escola(d):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=d, x='EducationLevel', hue='Alzheimer')
    plt.title('Relação de Alzheimer e Escolaridade')
    plt.xlabel('Nível de Estudo')
    plt.ylabel('Contagem')
    plt.show()

def grafico_idade(d):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=d[d['Alzheimer'] == 'Nao'], x='Age', kde=True, color='green')
    plt.title('Distribuição de Idade - Pacientes Saudáveis')
    plt.xlabel('Anos')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(data=d[d['Alzheimer'] == 'Sim'], x='Age', kde=True, color='red')
    plt.title('Distribuição de Idade - Pacientes com Alzheimer')
    plt.xlabel('Anos')
    plt.show()

def grafico_balanco(d):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=d, x='Alzheimer', hue='Alzheimer', palette=['green', 'red'], legend=False)
    plt.title('Total de Pacientes em Relação ao Alzheimer')
    plt.xlabel('Confirmacao de Alzheimer')
    plt.show()

def grafico_mmse(d):
    plt.figure(figsize=(12, 7))
    sns.boxplot(data=d, x='EducationLevel', y='MMSE', hue='Alzheimer')
    plt.title('Score Cognitivo por Estudo e Alzheimer')
    plt.ylabel('MMSE')
    plt.text(0.5, -0.12, 'MMSE (Baixo = Pior)', ha='center', va='center', transform=plt.gca().transAxes, weight='bold')
    plt.show()

def rodar():
    df = carregar()
    
    print(f"Base: {len(df)} | Dups: {df['PatientID'].duplicated().sum()} | Docs: {df['DoctorInCharge'].nunique()}")

    grafico_genero(df)
    grafico_etnia(df)
    grafico_escola(df)
    grafico_idade(df)
    grafico_balanco(df)
    grafico_mmse(df)

if __name__ == "__main__":
    rodar()
