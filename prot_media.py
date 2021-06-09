import collections
import pandas as pd
import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

dataset = pd.read_csv(dir_path+'\\CSVs_filtros\\filtros_Carisma\\Carisma_SEM_FILTRO.csv',sep=",")

#print(dataset)

dataset_mean = dataset.mean()

#print(dataset_mean)
#exit()

data = {'Questao': ['Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26']}

lst_filtros = [
'_SEM_FILTRO',
'_Familiar_Sim',
'_Familiar_Nao',
'_Fem',
'_Masc',
'_Idade_Menor_30',
'_Idade_Maior_30',
'_Escolaridade_EMI_EMC_SI',
'_Escolaridade_SC_PGC',
]

df = pd.DataFrame(data)

for filtro in lst_filtros:
    df_filtro = pd.read_csv(dir_path+'\\CSVs_filtros\\filtros_Carisma\\Carisma'+filtro+'.csv',sep=',')
    df_filtro_media = df_filtro.mean()

    lista = []
    for media in df_filtro_media:
        lista.append(media)
    df[filtro] = lista

print(df)

df.to_csv(dir_path+'\\teste.csv',index=False)



""" print("++++++++++++++++++++++++++++\n")
print(filtro)
print(df_filtro_media)
print("\n++++++++++++++++++++++++++++\n") """


#lista=[]

""" 
for i in dataset_mean:
    lista.append(i)
 """
#print(lista)

#df['teste'] = lista
#print(df)


""" 
                Q1  Q2  Q3  Q4  Q5  Q6

semFiltro       medias
Fem         
Masc 
Fam_Sim
Fam_Nao
menor_30
maior_30
emi_emc_si
sc_pgc

Questao        semFiltro    Fem    Masc    Fam_Sim     Fam_Nao     menor_30    maior_30    emi_emc_si      sc_pg

        
Q1
Q2
Q3
Q4
Q5
Q6
 """

#conforto_dataset_mean.to_csv('C:/Users/lucas.andreotti/Desktop/03 - Integradora/DadosFormulario/Analise_Conforto_Carisma/python_Carisma/media_formatado_semFiltro_Conforto.csv', index=False)