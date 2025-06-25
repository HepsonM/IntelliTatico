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

