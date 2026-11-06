# Demandas360 — Painel de gestão de demandas

Aplicação web demonstrativa para acompanhar solicitações de diferentes áreas em um quadro Kanban, com indicadores, filtros e busca.

## Funcionalidades
- Quadro com três estados de fluxo.
- Indicadores consolidados.
- Filtro por área e busca por código ou título.
- API REST para demandas, áreas e resumo.
- Dataset sintético versionado no projeto.

## Tecnologias
Python, Flask, HTML, CSS e JavaScript (Vanilla).

## Executar localmente
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Abra http://127.0.0.1:5000.

## Endpoints
- `GET /api/demandas`
- `GET /api/demandas?area=Dados`
- `GET /api/demandas?status=Concluído`
- `GET /api/demandas?q=conversão`
- `GET /api/areas`
- `GET /api/resumo`

## Dados e escopo
Todos os registros são fictícios. A aplicação não se conecta a Jira ou qualquer sistema corporativo. Este projeto é uma implementação independente para demonstração de competências.
