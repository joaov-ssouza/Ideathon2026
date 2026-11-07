def analisar_impacto_rota(distancia_metros: float, severidade: str, categoria: str) -> dict:
    """
    Heurística simples para o Ideathon.
    Avalia o risco de uma ocorrência baseada na distância do itinerário e severidade.
    """
    risco = "Baixo"
    atraso_estimado = "0 a 2 minutos"
    
    if distancia_metros <= 200:
        if severidade == "Alta":
            risco = "Alto"
            atraso_estimado = "15 a 30 minutos"
        elif severidade == "Moderada":
            risco = "Moderado"
            atraso_estimado = "5 a 10 minutos"
    elif distancia_metros <= 1000:
        if severidade == "Alta":
            risco = "Moderado"
            atraso_estimado = "5 a 10 minutos"
            
    mensagem = f"{categoria} próxima ao itinerário. {risco} risco de impacto. Atraso demonstrativo estimado entre {atraso_estimado}."
    
    return {
        "risco": risco,
        "mensagem": mensagem,
        "cor_alerta": "red" if risco == "Alto" else ("orange" if risco == "Moderado" else "green")
    }