# IntelliTatico

Sistema modular para gerar cortes automáticos de jogos de futebol com análise tática utilizando IA.

## Estrutura

```
src/
  event_detection.py      # funções para identificar eventos críticos via SofaScore
  streamlit_app.py        # interface visual para seleção do jogo e visualização de cortes
  services/
    sofascscore.py        # integração básica com SofaScore
  pipelines/
    video_pipeline.py     # pipeline de corte e análise (esboço)
```

## Dependências
As dependências principais estão em `requirements.txt`.
Instale com:

```bash
pip install -r requirements.txt
```

## Executando

```bash
streamlit run src/streamlit_app.py
```


## Arquitetura

O projeto está dividido em módulos independentes para facilitar extensão:

- `services/` contem wrappers para integração com APIs externas como SofaScore.
- `event_detection.py` concentra lógica de busca de eventos críticos de uma partida.
- `pipelines/` possui pipelines de processção de vídeo para gerar os cortes.
- `streamlit_app.py` oferece uma interface simples para seleção do jogo e visualização dos clipes.

### Pipeline básica

1. `search_match` localiza a partida no SofaScore.
2. `fetch_critical_events` baixa incidentes relevantes.
3. `VideoPipeline.process_events` recorta o vídeo baseando-se nos minutos dos eventos.

Essa estrutura serve de ponto inicial para evoluir com detecção de jogadas via visão computacional e análise tática com IA.

