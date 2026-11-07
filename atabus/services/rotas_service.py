def calcular_rota_simulada(origem_id: str, destino_id: str) -> list[dict]:
    """
    Calcula até 3 alternativas de rotas (direta ou com baldeação)
    com base nas localizações selecionadas pelo utilizador.
    """
    if not origem_id or not destino_id or origem_id == destino_id:
        return []

    return [
        {
            "id": "rota-1",
            "tipo": "Linha Direta",
            "linha": "Linha 104 - Guanabara / Centro",
            "tempo_total": "18 min",
            "espera": "4 min",
            "caminhada": "3 min (250m)",
            "baldeacao": False,
            "troca_linha": None,
            "acessivel": True,
            "seguranca_nota": "4.8/5",
            "recomendada": True,
        },
        {
            "id": "rota-2",
            "tipo": "Com 1 Baldeação",
            "linha": "Linha 102 → Linha 205",
            "tempo_total": "24 min",
            "espera": "2 min",
            "caminhada": "5 min (400m)",
            "baldeacao": True,
            "troca_linha": "Terminal Urbano Central",
            "acessivel": True,
            "seguranca_nota": "4.2/5",
            "recomendada": False,
        }
    ]