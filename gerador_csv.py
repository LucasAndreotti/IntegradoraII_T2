import collections
import pandas as pd

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

dir_path_src = dir_path + '\\CSVs_formatado'

def padronizador(dataset,tipo):

    #print((dataset.columns))
 
    #Padroniza as colunas

    colunasFixas = ['Genero', 'Faixa_Etaria', 'Escolaridade', 'Familiaridade']
    colunasParte1 = ['Q1','Q2','Q3','Q4','Q5','Q6']
    colunasParte2 = ['Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26']

    if tipo==1:
        dataset.columns = (colunasFixas+colunasParte1)
    else:
        dataset.columns = (colunasFixas+colunasParte2)
    #print(dataset.columns)

    #Padroniza Faixa Etária
    dataset = dataset.replace('18 até 20 anos', '18-20')
    dataset = dataset.replace('21 até 29 anos', '21-29')
    dataset = dataset.replace('30 até 39 anos', '30-39')
    dataset = dataset.replace('40 até 49 anos', '40-49')
    dataset = dataset.replace('50 até 59 anos', '50-59')
    dataset = dataset.replace('Acima de 60 anos', '60')

    #Padroniza Escolaridade
    dataset = dataset.replace('Superior Completo', 'SC')
    dataset = dataset.replace('Ensino Médio Completo', 'EMC')
    dataset = dataset.replace('Pós-Graduação Completa', 'PGC')
    dataset = dataset.replace('Superior Incompleto', 'SI')
    dataset = dataset.replace('Ensino Médio Incompleto', 'EMI')

    #Padroniza Familiaridade
    dataset = dataset.replace('Não','Nao')

    return dataset

def carisma():

    carisma_dataset = pd.read_csv(dir_path+"\\CSVs_original\\semFiltro_Carisma.csv", sep=';')
    #print(carisma_dataset)
    #print((carisma_dataset.columns))

    carisma_dataset = padronizador(carisma_dataset,2)

    carisma_dataset = carisma_dataset.replace("Muito carismático", 5)
    carisma_dataset = carisma_dataset.replace("Carismático", 4)
    carisma_dataset = carisma_dataset.replace("Normal", 3)   
    carisma_dataset = carisma_dataset.replace("Pouco carismático", 2)
    carisma_dataset = carisma_dataset.replace("Sem carisma", 1)

    carisma_dataset.to_csv(dir_path_src+'\\formatado_semFiltro_Carisma.csv', index=False)
    #print(carisma_dataset)

    #carisma_dataset_mean = carisma_dataset.mean()
    #carisma_dataset_mean.to_csv('C:/Users/lucas.andreotti/Desktop/03 - Integradora/DadosFormulario/Analise_Conforto_Carisma/python_Carisma/media_formatado_semFiltro_Carisma.csv', index=False)

def conforto():

    conforto_dataset = pd.read_csv(dir_path+"\\CSVs_original\\semFiltro_Conforto.csv", sep=';')
    #print(conforto_dataset)
    #print((conforto_dataset.columns))

    conforto_dataset = padronizador(conforto_dataset,2)

    conforto_dataset = conforto_dataset.replace("Muito confortável", 5)
    conforto_dataset = conforto_dataset.replace("Confortável", 4)
    conforto_dataset = conforto_dataset.replace("Normal", 3)
    conforto_dataset = conforto_dataset.replace("Desconfortável", 2)
    conforto_dataset = conforto_dataset.replace("Muito desconfortável", 1)

    conforto_dataset.to_csv(dir_path_src+'\\formatado_semFiltro_Conforto.csv', index=False)
    #print(conforto_dataset)

    #conforto_dataset_mean = conforto_dataset.mean()
    #conforto_dataset_mean.to_csv('C:/Users/lucas.andreotti/Desktop/03 - Integradora/DadosFormulario/Analise_Conforto_Carisma/python_Carisma/media_formatado_semFiltro_Conforto.csv', index=False)

def acertos_Parte1():
    parte1_dataset = pd.read_csv(dir_path+"\\CSVs_original\\semFiltro_Parte1.csv", sep=';')
    parte1_dataset = padronizador(parte1_dataset,1)

    parte1_dataset = parte1_dataset.replace("Apenas um rosto neutro", "Neutro")
    parte1_dataset = parte1_dataset.replace("Não sei (percebi uma expressão, mas não sei qual)", "Nao_Sei")
    parte1_dataset = parte1_dataset.replace("Não sei (percebi uma expressão mas não sei qual)", "Nao_Sei")

    parte1_dataset.to_csv(dir_path_src+'\\formatado_semFiltro_Parte1.csv', index=False)



""" def acertos_Parte2(): """



def acertos_Parte2A():
    parte2A_dataset = pd.read_csv(dir_path+"\\CSVs_original\\semFiltro_Parte2A.csv", sep=';')
    parte2A_dataset = padronizador(parte2A_dataset,2)

    parte2A_dataset = parte2A_dataset.replace("Nenhuma (não percebi nada a mais)", "Nenhuma")
    parte2A_dataset = parte2A_dataset.replace("Eu não sei (eu percebi alguma coisa mas não sei o que)", "Nao_sei")

    parte2A_dataset.to_csv(dir_path_src+'\\formatado_semFiltro_Parte2A.csv', index=False)

def acertos_Parte2B():
    parte2B_dataset = pd.read_csv(dir_path+"\\CSVs_original\\semFiltro_Parte2B.csv", sep=';')
    parte2B_dataset = padronizador(parte2B_dataset,2)

    parte2B_dataset = parte2B_dataset.replace("Nenhuma (não percebi nada a mais)", "Nenhuma")
    parte2B_dataset = parte2B_dataset.replace("Eu não sei (eu percebi alguma coisa mas não sei o que)", "Nao_sei")

    parte2B_dataset.to_csv(dir_path_src+'\\formatado_semFiltro_Parte2B.csv', index=False)


carisma()
conforto()
acertos_Parte1()
acertos_Parte2A()
acertos_Parte2B()



