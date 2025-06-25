# IntelliTatico

Sistema modular para gerar cortes automáticos de jogos de futebol com análise tática utilizando IA.

Esta base contém um esboço inicial do projeto com capacidade de buscar um jogo a partir dos nomes dos times utilizando a API não oficial do SofaScore. O processo de corte em vídeo ainda é um "TODO", mas a estrutura modular já permite evoluções rápidas.

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

Ao abrir o app, informe o nome dos dois times e clique em **Find match** para que o ID do jogo seja buscado automaticamente.

