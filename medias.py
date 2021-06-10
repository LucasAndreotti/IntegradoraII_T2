
import collections
import pandas as pd
import numpy as np
import os

from pandas.core.frame import DataFrame

dir_path = os.path.dirname(os.path.realpath(__file__))

dir_path_from = dir_path + '\\CSVs_filtros'

dir_path_to = dir_path + '\\CSVs_medias'

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

dic = { 'pp':'pos_pos','pn':'pos_neg','nn':'neg_neg','np':'neg_pos'}

dic_alias = {
7  :	'pn', 
8  :	'pn' ,
9  :	'np' ,
10 :	'nn' ,
11 :	'np' ,
12 :	'nn' ,
13 :	'nn' ,
14 :	'pn' ,
15 :	'pp' ,
16 :	'pn' ,
17 :    'nn' ,
18 : 	'np' ,
19 :	'np' ,
20 : 	'np' ,
21 :	'pp' ,
22 :	'nn' ,
23 :	'nn' ,
24 :	'nn' ,
25 :	'pn' ,
26 :	'np' }

def mediaDosFiltros(nome):
    if nome == 'Parte1':
        dataset_medias = {'Questao': ['Q1','Q2','Q3','Q4','Q5','Q6','Media_Medias']}
    else:
        dataset_medias = {'Questao' : ['Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','Media_Medias','Media_pp','Media_pn','Media_nn','Media_np']}

    dataset_medias = pd.DataFrame(dataset_medias)
    
    path = dir_path_from+'\\filtros_'+nome+'\\'+nome

    for filtro in lst_filtros:
        dataset_filtro = pd.read_csv(path+filtro+'.csv',sep=',')
        dataset_filtro_media = dataset_filtro.mean()

        lst_medias = dataset_filtro_media.tolist()
        media_medias = dataset_filtro_media.mean()
        lst_medias.append(media_medias)

        if nome != 'Parte1':
            n_questao = 7
            media_pp = []
            media_pn = []
            media_nn = []
            media_np = []

            for i in range(len(lst_medias)-1):
                print(n_questao)
                if(dic[dic_alias[n_questao]]=='pos_pos'):
                    media_pp.append(lst_medias[i])
                elif(dic[dic_alias[n_questao]]=='pos_neg'):
                    media_pn.append(lst_medias[i])
                elif(dic[dic_alias[n_questao]]=='neg_neg'):
                    media_nn.append(lst_medias[i])
                else:    
                    media_np.append(lst_medias[i])
                n_questao+=1

            media_pp = sum(media_pp)/len(media_pp)
            media_pn = sum(media_pn)/len(media_pn)
            media_nn = sum(media_nn)/len(media_nn)
            media_np = sum(media_np)/len(media_np)

            lst_medias.append(media_pp)
            lst_medias.append(media_pn)
            lst_medias.append(media_nn)
            lst_medias.append(media_np)

        for i in range(len(lst_medias)):
            lst_medias[i] = ("{:.4f}".format(lst_medias[i]).replace('.',','))

        dataset_medias[filtro]=lst_medias

    dataset_medias.to_csv(dir_path_to+'\\medias_'+nome+'.csv',index=False,sep=';')

##

mediaDosFiltros('Parte2A')

""" lst_partes = ['Parte1','Parte2A','Parte2B','Carisma','Conforto']
for parte in lst_partes:
    mediaDosFiltros(parte)  """



""" 
        semFiltro    Fem    Masc    Fam_Sim     Fam_Nao     menor_30    maior_30    emi_emc_si      sc_pg

        
Q1
Q2
Q3
Q4
Q5
Q6
 """