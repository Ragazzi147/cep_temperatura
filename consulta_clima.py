import requests

def obter_dados_inmet_por_cep(cep):
    # Usando o serviço ViaCEP para obter o código do município a partir do CEP
    url_cep_para_municipio = f'https://viacep.com.br/ws/{cep}/json/'
    response_cep = requests.get(url_cep_para_municipio)

    if response_cep.status_code != 200:
        return "Erro ao obter código do município a partir do CEP"

    data_cep = response_cep.json()
    codigo_municipio = data_cep.get('ibge')

    if not codigo_municipio:
        return "Código do município não encontrado"

    # Consultando a API do INMET para obter os dados da estação meteorológica
    url_inmet = f'https://apiprevmet3.inmet.gov.br/estacao/proxima/{codigo_municipio}'
    response_inmet = requests.get(url_inmet)

    if response_inmet.status_code != 200:
        return "Erro ao obter dados da estação meteorológica"

    data_inmet = response_inmet.json()
    temperatura_instantanea = data_inmet['dados']['TEM_INS']
    umidade_instantanea = data_inmet['dados']['UMD_INS']

    return f'Temperatura: {temperatura_instantanea}°C\nUmidade: {umidade_instantanea}%'

if __name__ == "__main__":
    cep = input("Digite o CEP: ")
    resultado = obter_dados_inmet_por_cep(cep)
    print(resultado)
