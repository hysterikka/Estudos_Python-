import geopandas as gpd
import sqlite3

def kml_to_sqlite(kml_file, sqlite_file, table_name):
    # Lê o arquivo KML usando geopandas
    gdf = gpd.read_file(kml_file, driver='KML')

    # Conecta-se ao banco de dados SQLite
    conn = sqlite3.connect(sqlite_file)
    
    # Salva o GeoDataFrame no SQLite
    gdf.to_sql(table_name, conn, if_exists='replace', index=False, index_label='id')

    # Fecha a conexão
    conn.close()

if __name__ == "__main__":
    # Substitua 'seu_arquivo.kml', 'seu_banco_de_dados.sqlite' e 'sua_tabela' pelos valores desejados
    kml_file = 'seu_arquivo.kml'
    sqlite_file = 'seu_banco_de_dados.sqlite'
    table_name = 'sua_tabela'

    kml_to_sqlite(kml_file, sqlite_file, table_name)
