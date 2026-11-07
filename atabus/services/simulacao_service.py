import reflex as rx
from sqlmodel import select
from ..modelos.entidades import Parada, Linha, Ocorrencia

class EstadoSeed(rx.State):
    def popular_banco(self):
        """Popula o banco de dados apenas se ele estiver vazio."""
        with rx.session() as session:
            linhas = session.exec(select(Linha)).all()
            
            if not linhas:
                session.add_all([
                    Linha(codigo="104", nome="Guanabara / Centro", origem="Shopping Praça Nova", destino="Assaí Atacadista"),
                    Linha(codigo="102", nome="Centro / Bairro", origem="Centro", destino="Bairro")
                ])
                
                session.add_all([
                    Parada(nome="Shopping Praça Nova", latitude=-21.2185, longitude=-50.4350, acessivel=True, cobertura=True, iluminacao=True),
                    Parada(nome="Assaí Atacadista", latitude=-21.1990, longitude=-50.4150, acessivel=True, cobertura=True, iluminacao=False)
                ])
                
                session.add_all([
                    Ocorrencia(categoria="Interrupção", descricao="Obras na via", linha_afetada="102", severidade="Alta"),
                    Ocorrencia(categoria="Alagamento", descricao="Ponto de alagamento na Avenida", linha_afetada="104", severidade="Alta")
                ])
                
                session.commit()