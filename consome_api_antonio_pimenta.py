# Nome do programa: consome_api_antonio_pimenta.py
import requests
import xml.etree.ElementTree as ET

# URL da API fornecida
URL_API = "http://instituto.islagaia.pt/ws/wsrifa.asmx/Rifa"

def invocar_api():
    try:
        # Invoca a API e retorna o resultado
        resposta = requests.get(URL_API)
        if resposta.status_code == 200:
            print("API invocada com sucesso!")
            return resposta.text  # Retorna o conteúdo da resposta como texto
        else:
            print(f"Erro na API: {resposta.status_code}")
            return None
    except Exception as e:
        print(f"Erro ao invocar a API: {e}")
        return None

def extrair_resultado(resposta_texto):
    # Parseia o XML e ignora o namespace
    if resposta_texto:
        # Remover a declaração do XML, se existir
        resposta_texto = resposta_texto.replace("<?xml version=\"1.0\" encoding=\"utf-8\"?>", "")
        
        # Parseando o XML com ElementTree
        root = ET.fromstring(resposta_texto)
        
        # Ignorando o namespace ao buscar o valor da tag <string>
        # Pode ser necessário ajustar o nome da tag dependendo da resposta real
        for elem in root.iter("{http://tempuri.org/}string"):  # Ignora o namespace
            return elem.text.strip()
    return "N/A"

def main():
    print("### Programa: consome_api_antonio_pimenta.py ###")
    resultado_api = invocar_api()
    if resultado_api:
        # Extrai o valor da resposta
        resultado = extrair_resultado(resultado_api)
        # Exibe o resultado formatado
        print(f"Resultado do sorteio: {resultado}")
    else:
        print("Não foi possível obter dados da API.")

if __name__ == "__main__":
    main()


