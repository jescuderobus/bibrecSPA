# Esta versión añáde la columna Annyo al json generado 

import json, sys
import pandas as pd

if __name__ == "__main__":
    assert len(sys.argv) > 1, "Debe introducir la ruta del fichero de origen."

    filepath = sys.argv[1]

    data = pd.read_csv(filepath)
    data['Ordenar'] = data['Centro'].str.lower()
    data = data.sort_values(['Ordenar','Titulacion','Codigo'])
    columnas_buenas = data[['Centro','Titulacion','Codigo','Asignatura','Annyo']]
    res = {}
    for entrada in columnas_buenas.iterrows():
        centro = entrada[1]['Centro']
        titulacion = entrada[1]['Titulacion']
        codigo = entrada[1]['Codigo']
        asignatura = entrada[1]['Asignatura']
        anio = entrada[1]['Annyo']
        if centro not in res:
            res[centro] = {titulacion:[{'ca':codigo,'da':asignatura,'an':anio}]}
        else:
            if titulacion not in res[centro]:
                res[centro][titulacion] = [{'ca':codigo,'da':asignatura,'an':anio}]
            else:
                res[centro][titulacion].append({'ca':codigo,'da':asignatura,'an':anio})
    with open('./code/bibrec24actulizado.json','w',encoding='utf8') as f:
        json.dump(res,f)