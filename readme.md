# Bem-vindo ao AtaBus!

Este é o repositório do nosso projeto AtaBus no *Ideathon 2026.2* da Fatec de Araçatuba. Dê uma olhada nos códigos, rascunhos, organização das pastas, arquitetura aplicada, fundamentações e demais itens importantes por aqui.

## Tecnologias

- **Desenvolvimento Web:** Reflex
- **Ambiente de Produção:** Docker
- **Cloud/Deploy:** Render

## Documentação

- [Anotações "Extra" dos integrantes](https://docs.google.com/document/d/1AI1gTw0tbduEZQlvfL1OGX0-l26k6E2nWRDeNd40sHA/)
- [Prototipação Navegável](https://atabus.onrender.com/)
- [Protótipo Estático (Figma)](https://www.figma.com/design/nCsOBl7Y9qz3dUgYGwaNt0/%C3%94nibus?node-id=0-1&t=GKc25aofybLvRKxU-1)
- [Declaração de Originalidade e Uso de IA](https://docs.google.com/document/d/1-z9S7Kji2Z0binJS_tDtquUJRqxTQQOMx6yC2l1XNuI/edit?usp=sharing)
- [Apresentação](https://canva.link/htwn9hwpa17l0ae)

## Membros (2º Semestre)

- Eduardo Augusto Santos Rocha
- Gabriel Carvalho dos Santos Camargo
- João Vitor Santiago Souza
- João Pedro Silva Lima
- Ruan Luiz Antunes Melo

## Problema

O modelo atual de transporte coletivo trata todos os passageiros como iguais, ignorando que cada pessoa tem necessidades únicas de deslocamento. O grande gargalo não é apenas descobrir "onde o ônibus está", mas a profunda falta de autonomia e previsibilidade. Passageiros são forçados a seguir trajetos rígidos e desinformados, que não consideram se o caminho até o ponto é seguro, se exige muito esforço físico ou se atende a restrições de mobilidade. Essa incerteza diária rouba tempo, gera insegurança (especialmente para grupos vulneráveis) e torna o transporte público uma opção engessada.

## Solução

O AtaBus não é apenas mais um aplicativo de mapas — é uma plataforma de mobilidade personalizada e previsível. Nosso diferencial é devolver o poder de decisão ao usuário. 

Ao invés de apenas mostrar rotas, o AtaBus permite que o passageiro defina seus próprios critérios de viagem, priorizando sua segurança pessoal, menor esforço físico, tempo reduzido ou conveniência da localidade. A plataforma cruza essas preferências com avaliações colaborativas dos pontos de parada, entregando o trajeto ideal para o perfil específico daquela pessoa. Tudo isso atrelado a um sistema de previsibilidade real, garantindo que o usuário saiba exatamente quando sair de casa, maximizando sua segurança e seu tempo.

## Próximos Passos

- **Modelos Reais de Machine Learning (ML):** Substituir as lógicas iniciais por algoritmos de ML robustos que aprendam com o histórico de uso, refinando dinamicamente o mapeamento de rotas e prevendo padrões de atraso.
- **Expansão de Escopo (Intermunicipal e Multimodal):** Levar a arquitetura do AtaBus para rodovias e viagens intermunicipais para criar jornadas completas.
- **Dados em Tempo Real:** Integração contínua com APIs de GPS e telemetria da frota real da cidade.

## Limitações Conhecidas (MVP)

Sendo este um Produto Mínimo Viável (MVP) desenvolvido durante o Ideathon:
- **Dados Simulados:** O software atualmente roda simulações estáticas em ambiente controlado (mock de dados) para demonstrar a viabilidade da arquitetura, não consumindo posicionamento GPS real da frota neste estágio.
- **Algoritmos Iniciais:** O motor de sugestão de rotas baseado nas preferências do usuário atua com lógica simulada; o treinamento real com Machine Learning faz parte da visão de futuro.
- **Estética e UI:** O design atual atende a um protótipo de alta fidelidade funcional, com refinamentos estéticos e de usabilidade profunda mapeados para as próximas fases de evolução do produto.

## Como Rodar Localmente

Para testar a aplicação na sua própria máquina, siga os passos abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SEU_USUARIO/atabus.git
   cd atabus
   ```

2. **Crie e ative um ambiente virtual (Recomendado):**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie a aplicação:**
   ```bash
   reflex run
   ```
   *O aplicativo estará disponível no seu navegador em `http://localhost:3000`.*