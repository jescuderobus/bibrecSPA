# bibrecSPA

Esta aplicación crea una página web con un formulario que permite buscar en fama.us.es la bibliografia de las asignaturas que se cursan en la US.


## Creación del fichero con todas las asignaturas

A partir de un fichero CSV que contenga para cada asignatura, el codigo asignado a la asignatura, la titulación a la que pertenece y el centro en el que se imparte, generamos un fichero JSON.

Para generarlo hay que ejecutar el fichero Python mediante el comando:

`python create_json.py <RUTA_CSV> <RUTA_JSON>`

Que personalizado para nuestro entorno sería:

`python3 code/create_json.py code/BIBREC23.csv code/bibrec23.json`

Si el fichero no existe puede que sea recomendable crearlo vacio previamente.


## Versiones

bibrec24_25v2.html --> recoge parámetros via GET para hacer consultas predeterminadas

https://biblus.us.es/bib2/bibrec/index.php?palabra=Grado+en+Ingenier%C3%ADa+Aeroespacial&varbusqueda=titulacion&buscador=Buscar&tipo=todo&termino=Grado+en+Ingenier%C3%ADa+Aeroespacial

http://127.0.0.1:3000/index.html?optone=E.T.S.+de+Ingenier%C3%ADa&opttwo=Grado+en+Ingenier%C3%ADa+Aeroespacial


