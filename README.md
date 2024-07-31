# bibrecSPA

Esta aplicación crea una página web con un formulario que permite buscar en fama.us.es la bibliografia de las asignaturas que se cursan en la US.


## Creación del fichero con todas las asignaturas

A partir de un fichero CSV que contenga para cada asignatura, el codigo asignado a la asignatura, la titulación a la que pertenece y el centro en el que se imparte, generamos un fichero JSON.

Para generarlo hay que ejecutar el fichero Python mediante el comando:

`python create_json.py <RUTA_CSV> <RUTA_JSON>`

Que personalizado para nuestro entorno sería:

`python3 code/create_json.py code/BIBREC23.csv code/bibrec23.json`

Si el fichero no existe puede que sea recomendable crearlo vacio previamente.


