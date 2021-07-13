## UTILS
import pandas as pd
import numpy as np
import graphviz
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split

RANDOM_STATE = 19 * 103785

## Auxiliares
GSPREADHSEET_DOWNLOAD_URL = ("https://docs.google.com/spreadsheets/d/{gid}/export?format=csv&id={gid}".format)

DF_TRAIN_GID = '1-DWTP8uwVS-dZY402-dm0F9ICw_6PNqDGLmH0u8Eqa0'
DF_HOLDOUT_GID = "1ObsojtXfzvwicsFieGINPx500oGbUoaVTERTc69pzxE"

def obtenerDF(GID):
    return pd.read_csv(GSPREADHSEET_DOWNLOAD_URL(gid=GID), skiprows=0)

def obtenerDFTraining():
    return obtenerDF(DF_TRAIN_GID)

def obtenerDFHoldout():
    return obtenerDF(DF_HOLDOUT_GID)

# Imprime las metricas Recall, Precision, Accuracy, Roc-auc y muestra la matriz de confuncion.
def metricas(y_real, y_pred, x_test, modelo):

    data = {'y_real': y_real,
            'y_pred': y_pred}

    df_metricas = pd.DataFrame(data, columns=['y_real','y_pred'])
    confusion_matrix = pd.crosstab(df_metricas['y_real'], df_metricas['y_pred'], rownames=['Real'], colnames=['Predicho'])
    sns.heatmap(confusion_matrix, annot=True, fmt="d")
    plt.show()

    print("Recall: {}".format(recall_score(y_real, y_pred).round(2)))
    print("Precision: {}".format(precision_score(y_real, y_pred).round(2)))
    print("Acc: {}".format(accuracy_score(y_real, y_pred).round(2)))
    print("Roc: {}".format(roc_auc_score(y_real, modelo.predict_proba(x_test)[:, 1]).round(2)))
    return

def escribir_predicciones_a_archivo(predicciones:np.array, nombre_modelo, ids):
    archivo = open("PrediccionesHoldout/"+nombre_modelo+".csv", "w")
    archivo.write("id,tiene_alto_valor_adquisitivo\n")
    i = 0
    for prediccion in predicciones:
        archivo.write(str(ids[i])+ "," + str(prediccion) + "\n")
        i = i + 1
    archivo.close()

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

def prepros_dummies(data):
    
    data_prepos = pd.get_dummies(data, drop_first=True)
    return data_prepos

def preprocesar_variables_numericas(df):
    df['ganancia_perdida_declarada_bolsa_argentina'] = df['ganancia_perdida_declarada_bolsa_argentina'].apply(lambda x: np.tanh(x))
    return df

def preprocesar_df_min_max_scaler(X : pd.DataFrame):
    X = pd.get_dummies(X, drop_first=True)
    scaler = MinMaxScaler()
    scaler.fit(X)
    return scaler.transform(X)

def preprocesar_df_pca(X, dim):
    pca = PCA(dim)
    X_trans = pd.DataFrame(pca.fit_transform(X))
    return X_trans 

def preprocesar_standar_scaler(X : pd.DataFrame):
    scaler = StandardScaler()
    scaler.fit(X)
    return scaler.transform(X)

def preprocesar_normalize_scaler(X : pd.DataFrame):
    X = pd.get_dummies(X,drop_first= True) 
    scaler = Normalizer()
    scaler.fit(X)
    return scaler.transform(X)