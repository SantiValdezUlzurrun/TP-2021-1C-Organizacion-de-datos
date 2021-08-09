## Correciones

- Hacer dos preprocesamientos para todos los modelos, faltaría Bagging y Redes neuronales.-->CHECK

- Probar el kernel que les falta para el modelo de SVM. En cuanto a eso, para evitar que tarde demasiado pueden probar incrementando el valor de C, reduciendo las dimensiones (veo que probaron este preprocesamiento con Radial pero no se si con Lineal), y si nada de esto funciona pueden probar utilizando LinearSVC que es una implementación más eficiente pero solamente para este caso. -->CHECK

- Si bien en RandomForest cuando intentaron probar distintos valores de cantidad de estimadores para el modelo, el preprocesamiento tardaba demasiado, es fundamental que tengan en cuenta que es un hiperparámetro importante para este modelo. Tal vez con valores más pequeños podrían explorar otros valores sin que cuelgue. --->CHECK

- También les voy a pedir que agreguen una descripción a los gráficos que usan de análisis en Redes Neuronales explicando qué se ve en el mismo, por qué y cómo esto aporta a la configuraciones que hicieron a sus redes ---->CHECK


## Correciones Segunda tanda

- Si bien agregaron una descripción sobre los gráficos, esta sigue siendo muy general. La idea es que describan para cada gráfico qué está sucediendo en el mismo y cómo eso los motiva a probar algo distinto a continuación. Agreguen estas descripciones.-->CHECK

- No prueban diferentes hiperparámetros para este modelo. Sé que esta corrección se me escapó la primera vez, así que les pido mil disculpas pero es necesario que exploren diferentes valores de hiperparámetros antes de tomar la decisión sobre cuáles usar. Especialmente el número de estimadores. Agreguen esta exploración.-->CHECK