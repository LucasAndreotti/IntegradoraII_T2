import collections
import pandas as pd


def padronizador(dataset):

    #print((dataset.columns))

    #Padroniza as colunas
    dataset.columns = ['Genero', 'Faixa_Etaria', 'Escolaridade', 'Familiaridade', 'Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26']

    #print(dataset.columns)

    #Padroniza Faixa Etária
    dataset = dataset.replace('21 até 29 anos', '21-29')
    dataset = dataset.replace('18 até 20 anos', '18-20')
    dataset = dataset.replace('50 até 59 anos', '50-59')
    dataset = dataset.replace('40 até 49 anos', '40-49')
    dataset = dataset.replace('30 até 39 anos', '30-39')
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


carisma_dataset = pd.read_csv("C:/Users/lucas.andreotti/Desktop/03 - Integradora/DadosFormulario/Analise_Conforto_Carisma/python_Carisma/semFiltro_Carisma.csv", sep=';')
#print(carisma_dataset)
#print((carisma_dataset.columns))

carisma_dataset = padronizador(carisma_dataset)

carisma_dataset = carisma_dataset.replace("Muito carismático", 5)
carisma_dataset = carisma_dataset.replace("Carismático", 4)
carisma_dataset = carisma_dataset.replace("Normal", 3)
carisma_dataset = carisma_dataset.replace("Pouco carismático", 2)
carisma_dataset = carisma_dataset.replace("Sem carisma", 1)

#carisma_dataset.to_csv('C:/Users/lucas.andreotti/Desktop/03 - Integradora/DadosFormulario/Analise_Conforto_Carisma/python_Carisma/formatado_semFiltro_Carisma.csv', index=False)
#print(carisma_dataset)

carisma_dataset_mean = carisma_dataset.mean()


#carisma_dataset_mean.to_csv('C:/Users/lucas.andreotti/Desktop/03 - Integradora/DadosFormulario/Analise_Conforto_Carisma/python_Carisma/media_formatado_semFiltro_Carisma.csv', index=False)


#top_five_dataset['NomeColuna]
#top_five_dataset['NomeColuna].values
#top_five_dataset['NomeColuna].values[0]
#top_five_dataset = top_five_dataset[top_five_dataset['Top_2_Image'] == 7]
#top_five_dataset = top_five_dataset[top_five_dataset['Top_2_Image'] == 7]['NomeColuna]
#print(top_five_dataset)
#top_five_dataset = top_five_dataset.replace(7, "Muito Carismatico")
#print(top_five_dataset['Top_1_Image'])

#new_dic = {}

#new_dic['Image'] = top_five_dataset['Image'].values
#new_dic['Top_1_Image'] = top_five_dataset['Top_1_Image'].values
#new_df = pd.DataFrame(new_dic)
#new_df.to_csv('D:/Victor/UncannyValley/UncannyValley/UVImgs/UVImages/lucas.csv', index=False)





