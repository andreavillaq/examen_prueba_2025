import pandas as pd

def descargar_datos(ruta):
    df = pd.read_csv(ruta, sep=";")
    return df

def procesar_fecha(df):
    df['dt'] = pd.to_datetime(df['dt'])
    df['year'] = df['dt'].dt.year  
    return df

if __name__ == "__main__":
    ruta = r"C:\Users\andri\GitHub\examen_prueba_2025\data\datos_mock.csv"
    df = descargar_datos(ruta)
    df = procesar_fecha(df)
    print(df.head(5))
