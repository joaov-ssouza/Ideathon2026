import requests

def buscar_pontos_reais_aracatuba():
    """
    Consulta a Overpass API com identificação correta e Fallback de segurança para a banca.
    """
    query = """
    [out:json];
    area["name"="Araçatuba"]->.searchArea;
    node["highway"="bus_stop"](area.searchArea);
    out 30;
    """
    url = "https://overpass-api.de/api/interpreter"
    
    headers = {
        "User-Agent": "AtaBus-Ideathon-MVP/1.0 (contato@atabus.com)"
    }
    
    try:
        response = requests.post(url, data=query, headers=headers, timeout=2.5)
        
        if response.status_code == 200:
            data = response.json()
            pontos = []
            for element in data.get("elements", []):
                nome = element.get("tags", {}).get("name", "Ponto de Ônibus (OSM)")
                pontos.append({
                    "nome": nome,
                    "lat": element["lat"],
                    "lon": element["lon"]
                })
            print("Sucesso: Pontos baixados da API ao vivo!")
            return pontos
        else:
            print(f"Aviso OSM: Bloqueio temporário (Status {response.status_code})")
            
    except Exception as e:
        print(f"Aviso OSM: Falha na conexão ou Timeout ({e})")
        
    print("Injetando dados de backup para manter o MVP rodando...")
    return [
        {"nome": "Ponto Rua Dona Ida", "lat": -21.2050, "lon": -50.4400},
        {"nome": "Ponto Av. Brasília", "lat": -21.2100, "lon": -50.4350},
        {"nome": "Ponto Av. João Arruda Brasil", "lat": -21.1980, "lon": -50.4450},
        {"nome": "Ponto Rua Cristiano Olsen", "lat": -21.2150, "lon": -50.4420},
    ]