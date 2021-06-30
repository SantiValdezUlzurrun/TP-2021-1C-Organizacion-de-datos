## UTILS
import pandas as pd
import numpy as np


GSPREADHSEET_DOWNLOAD_URL = ("https://docs.google.com/spreadsheets/d/{gid}/export?format=csv&id={gid}".format)

DF_TRAIN_GID = '1-DWTP8uwVS-dZY402-dm0F9ICw_6PNqDGLmH0u8Eqa0'
DF_HOLDOUT_GID = "1ObsojtXfzvwicsFieGINPx500oGbUoaVTERTc69pzxE"

def obtenerDF(GID):
    return pd.read_csv(GSPREADHSEET_DOWNLOAD_URL(gid=GID), skiprows=0)

def obtenerDFTraining():
    return obtenerDF(DF_TRAIN_GID)

def obtenerDFHoldout():
    return obtenerDF(DF_HOLDOUT_GID)




## PREPROCESAMIENTO

def tiene_n_missings(x, n):
    acum = 0
    for i in range(len(x)):
        if x[i]:
            acum += 1
    return n <= acum


def feature_engineering(df):
    lista_de_missings = [tiene_n_missings(x, 3) for x in df.isna().to_numpy()]
    df_3_missings = df.reset_index()[lista_de_missings].set_index('index')
    df.drop(df_3_missings.index, inplace = True)
    df = df.replace({'trabajo': np.nan, 'categoria_de_trabajo': np.nan},'No contesto')
    df = df.replace({'barrio': np.nan},'Palermo')
    mapa = {'Palermo' : 'C14','Belgrano' : 'C13','San Isidro' : 'S.I','Villa Urquiza' : 'C12','Recoleta' : 'C2','La Boca' : 'C4','Agronomia' : 'C15','Almagro' : 'C5','Balvanera' : 'C3','Puerto Madero' : 'C1','Caballito' : 'C6','Boedo' : 'C5','Barracas' : 'C4','Chacarita' : 'C15','Coghland' : 'C12','Floresta' : 'C10','Constitucion' : 'C1','Colegiales' : 'C13','Flores' : 'C7','Liniers' : 'C9','Monte Castro' : 'C10','Mataderos' : 'C9','Nueva Pompeya' : 'C4','Monserrat' : 'C1','nuñez' : 'C13','Parque Chacabuco' : 'C7','Parque Avellaneda' : 'C9','Villa Luro' : 'C10','Parque Chas' : 'C15','La Paternal' : 'C15','Retiro' : 'C1','Villa Devoto' : 'C11','Villa Soldati' : 'C8','San Telmo' : 'C1','Villa Real' : 'C10','Santa Rita' : 'C11','Villa General Mitre' : 'C11','Versalles' : 'C10','Velez Sarsfield' : 'C10','Villa Pueyrredon' : 'C12','Cilla Riachuelo' : 'C8'}
    df['comuna'] = df['barrio'].apply(lambda x: mapa.get(x))
    df_gente_sin_trabajo_con_horas_registradas = df[(df['categoria_de_trabajo'] == 'sin_trabajo') & (df['horas_trabajo_registradas'] > 0)]
    df.drop(df_gente_sin_trabajo_con_horas_registradas.index, inplace = True)
    df['rol_familiar_registrado'] = df['rol_familiar_registrado'].apply(lambda x: 'casado' if x == 'casada' else x)
    df['estado_marital'] = df['estado_marital'].apply(lambda x: 'matrimonio' if x == 'matrimonio_civil' or x == 'matrimonio_militar' else x)
    df = df.drop(['educacion_alcanzada'],axis=1)
    return df

def preprocesar_data_frame(df : pd.DataFrame):
    df = feature_engineering(df)
    y = df['tiene_alto_valor_adquisitivo']
    X = df.drop(columns=['tiene_alto_valor_adquisitivo'])
    return (X, y)

    

    