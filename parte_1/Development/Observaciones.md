# TP

## Consideraciones iniciales

Inicialmente se clasificaron a las variables en influyentes o no, ademas de anotarse observaciones

### Influye en altos o bajos ingresos

- años estudiados
- categoria de trabajo
- edad (Ya sea por experiencia o falta de estudio)
- estado marital
- horas_de_trabajo_registradas
- trabajo
- ganancia


### No deberia influir

- Genero
- Barrio
- Religion

### Primeras observaciones

- Barrio mas del 90% es de Palermo
- Anios estudiados es un mapa de educacion alcanzada
- ganancia_perdida_declarada_bolsa_argentina el 87% es cero
- El 85% le gusta Jesus
- Probablemente rol_familiar y estado_marital esten relacionadas

-Segun nuestro arbolito mejorar el segundo if mejora muy poqco, en cambio nos queda por limpiar el otro, para limpiar el no del estado marital.

### Ranking Variables

 
1) .::Estado marital::. -
1 - 12|EM) .::Rol familiar::.-
2 - 12|EM - 12 |EM y T') horas de trabajo
3 - 2|EM - 1 |EM y T' ) anios_estudidados 
3 - 11|EM - 12|EM y T') Edad 
4 - 1 | EM - 12|EM y T' - 1|EM') Trabajo-

4 - 11|EM - 12|EM y T') Categoria de trabajo 
5 - 2|EM - 12|EM y T') Ganancia

4 - 12|EM - 12|EM y T' - 12|EM') Genero

11) Religion
11) Barrio

## PREGUNTAS

Gente con mas de 65 trabajando??
Combinar Matrimonios ??