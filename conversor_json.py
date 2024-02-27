import pandas as pd

def json_to_excel(json_file, excel_file, sheet_name='Sheet1'):
    # Lê o arquivo JSON usando pandas
    df = pd.read_json(json_file)

    # Salva o DataFrame em um arquivo Excel
    df.to_excel(excel_file, sheet_name=sheet_name, index=False)

if __name__ == "__main__":
    # Substitua 'seu_arquivo.json', 'sua_planilha.xlsx' e 'Sheet1' pelos valores desejados
    json_file = 'seu_arquivo.json'
    excel_file = 'sua_planilha.xlsx'
    sheet_name = 'Sheet1'

    json_to_excel(json_file, excel_file, sheet_name)
