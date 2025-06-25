# IntelliTatico

Sistema modular para gerar cortes automáticos de jogos de futebol com análise tática utilizando IA.

## Estrutura

```
src/
  event_detection.py      # funções para identificar eventos críticos via SofaScore
  streamlit_app.py        # interface visual para seleção do jogo e visualização de cortes
  services/
    sofascscore.py        # integração básica com SofaScore
    video_downloader.py   # utilitário para baixar vídeos
  pipelines/
    video_pipeline.py     # pipeline de corte e análise
    analysis.py           # esboço de análise tática
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

## Arquitetura sugerida

1. **Detecção de eventos**: `event_detection.fetch_critical_events` consulta a API do SofaScore e retorna apenas os incidentes relevantes.
2. **Download/streaming de vídeo**: `VideoDownloader` pode ser usado para obter o arquivo bruto do jogo.
3. **Corte e análise**: `VideoPipeline` recebe o vídeo completo e a lista de eventos, gerando clipes individuais para cada incidente. Etapas de visão computacional e análise por LLM podem ser acopladas nessa fase (ver `analysis.PlayAnalyzer`).
4. **Interface**: o aplicativo Streamlit permite selecionar o jogo, fazer upload do vídeo completo e assistir aos clipes gerados.

> **Nota**: para executar este projeto é necessário que as dependências estejam instaladas. Caso esteja em um ambiente sem acesso à internet, providencie um cache local dos pacotes ou ajuste o `requirements.txt` conforme sua disponibilidade.

