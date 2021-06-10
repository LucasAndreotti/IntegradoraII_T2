import collections
from textwrap import indent
import pandas as pd
import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

dir_path_from = dir_path + "\\CSVs_formatado"

dir_path_to = dir_path + "\\CSVs_corrigido"

def correcao(nome):

    dataset = pd.read_csv(dir_path_from+'\\formatado_semFiltro_'+nome+'.csv',sep=',')

    if nome == 'Parte1':

        lst_Questoes = ['Q1','Q2','Q3','Q4','Q5','Q6']
        lst_Respostas = ['Tristeza','Felicidade','Surpresa','Medo','Raiva','Desgosto']
        n_questoes = 6
    else:
        lst_Questoes = ['Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26']
        n_questoes = 20

        if (nome == 'Parte2A'):
            lst_Respostas = [
                'Felicidade','Surpresa','Tristeza','Medo'    ,'Raiva',
                'Medo'      ,'Tristeza','Surpresa','Surpresa','Felicidade',
                'Desgosto'  ,'Raiva'   ,'Medo'    ,'Desgosto','Felicidade',
                'Tristeza'  ,'Medo'    ,'Desgosto','Surpresa','Medo']
        else:
            lst_Respostas = [
                'Tristeza','Tristeza','Felicidade','Raiva'     ,'Felicidade',
                'Desgosto','Raiva'   ,'Medo'      ,'Felicidade','Raiva',
                'Tristeza','Surpresa','Surpresa'  ,'Surpresa'  ,'Surpresa',
                'Desgosto','Desgosto','Medo'      ,'Desgosto'  ,'Felicidade']

    for i in range(n_questoes):
        questao = lst_Questoes[i]
        dataset[questao] = np.where((dataset[questao] != lst_Respostas[i]),0,1)

    dataset.to_csv(dir_path_to+'\\corrigido_semFiltro_'+nome+'.csv',index=False)    

lst_partes = ['Parte1','Parte2A','Parte2B']

for parte in lst_partes:
    correcao(parte)

