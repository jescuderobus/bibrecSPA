import json, sys
import pandas as pd

if __name__ == "__main__":
    assert len(sys.argv) > 1, "Debe introducir la ruta del fichero de origen."
    assert len(sys.argv) > 2, "Debe introducir la ruta del fichero de destino."

    filepath_origen = sys.argv[1]
    filepath_destino = sys.argv[1]

    data = pd.read_csv(filepath_origen)
    data['Ordenar'] = data['Centro'].str.lower()
    data = data.sort_values(['Ordenar','Titulacion','Codigo'])
    columnas_buenas = data[['Centro','Titulacion','Codigo','Asignatura']]
    res = {}
    for entrada in columnas_buenas.iterrows():
        centro = entrada[1]['Centro']
        titulacion = entrada[1]['Titulacion']
        codigo = entrada[1]['Codigo']
        asignatura = entrada[1]['Asignatura']
        if centro not in res:
            res[centro] = {titulacion:[{'ca':codigo,'da':asignatura}]}
        else:
            if titulacion not in res[centro]:
                res[centro][titulacion] = [{'ca':codigo,'da':asignatura}]
            else:
                res[centro][titulacion].append({'ca':codigo,'da':asignatura})
    with open(filepath_destino,'w',encoding='utf8') as f:
        json.dump(res,f)