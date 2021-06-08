## Notas

#### Requisitos del TP
* Al menos 5 modelos
* Utilizar tecnicas para buscar los mejores hiper-parametros
* Al menos un ensamble
* Usar cross-validation para determinar el mejor modelo
* Todos los Modelos con metricas como: AUC-ROC, Matriz de confusión, Accuracy, Precisión, Recall
* Explicar el preprocesado/feature engineering
* Lógica del preprocesado en un archivo python llamado preprocesing.py
* Dos tecnicas de preprocesamiento distintos por cada tipo de modelo

Entrega:
* PDF con:
* (TABLA 1) Tabla que liste todos los pre-procesamientos utilizados, con el estilo:
<nombre preprocesamiento> < explicación simple> < nombre de la función de python >
* (TABLA 2) Tabla que liste:
<Nombre Modelo> <nombre preprocesamiento> <AUC-ROC> <Accuracy> <Precision> <Recall> <F1 score>
* Nombre Modelo este en un notebook separado con el nombre <Nombre Modelo>.ipynb y que dentro del mismo esté de forma clara la llamada a los preprocesados, su entrenamiento, la evaluación del mismo y finalmente una predicción en formato csv de un archivo nuevo localizado en: https://docs.google.com/spreadsheets/d/1ObsojtXfzvwicsFieGINPx500oGbUoaVTERTc69pzxE
* hagamos las predicciones de este archivo y en la entrega junto con los notebook también entreguemos todas las predicciones. El nombre del archivo con las predicciones tiene que ser <Nombre Modelo>.csv
* (CONCLUSIÓN)
* Todas las dependencias de librerías deben estar en un requirements.txt
* La entrega se tiene que realizar en el mismo repositorio de la primera entrega, en una carpeta llamada parte_2
* Las predicciones de cada modelo se deberan guardar en el directorio parte_2/predicciones


##### Modelos a hacer:

* Naive-Bayes
* KNN
* Arbol de decision
* Random-Forest
* SVM