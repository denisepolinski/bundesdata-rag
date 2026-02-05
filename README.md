# BUNDESDATA-RAG

**RAG-Pipeline für öffentliche Daten der Bundesbehörden**

Nutzung von APIs von bund.dev (z.B. Autobahnmeldungen, NINA, Bundestag, DWD) zur Informationsaufbereitung und Abfrage
mittels LLM.

In unserer Anwendung nutzen wir

## Zuständigkeiten

**Jonas Trenz (jtrenz):**

- API call setup (all important endpoints)
- Ollama Embedding Model setup
- Document indexing
- Finish gradio UI

**Denise Polinski:**

- project setup
- conversion of existing code to jupyter notebook
- conversion of loaded bundesdata from python objects (dict) to list of LangChain documents
- initial gradio UI

## Installationsanleitung
