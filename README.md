# BUNDESDATA-RAG

### RAG-Pipeline für öffentliche Daten der Bundesbehörden

Dieses Projekt implementiert ein **Retrieval-Augmented Generation (RAG)**-System
für **deutsche Autobahn-Bundesdaten**.  
Die Daten werden von `verkehr.autobahn.de` bezogen, in einer Vektordatenbank
gespeichert und über ein LLM (via Ollama) abfragbar gemacht.

Die gesamte Pipeline ist in einem **Jupyter Notebook (`.ipynb`)** umgesetzt.

## Zuständigkeiten

**Jonas Trenz (jtrenz):**

- blal

**Denise Polinski:**

- project setup
- conversion of existing code to jupyter notebook
- conversion of loaded bundesdata from python objects (dict) to list of LangChain documents
- initial gradio UI

## Installationsanleitung

1. **Repository clonen**

   ```bash
   git clone <https://github.com/denisepolinski/bundesdata-rag>

   cd bundesdata-rag

   ```

2. **Virtuelle Umgebung erstellen & Abhängigkeiten installieren**
   ```bash
   uv sync
   uv run jupyter notebook
   ```

Nach Ausführen der letzten Zeile startet automatisch das Gradio UI. Die URL wird im Notebook ausgegeben.
