from fastapi import FastAPI
from data import companies, knowledge
from llm import ask_llm

app = FastAPI()

@app.get("/")
def health():
    return {"status": "kundenAssistent läuft auf Render"}

@app.post("/chat")
def chat(company_id: str, question: str):
    company = companies.get(company_id)
    if not company:
        return {"answer": "Unternehmen nicht gefunden."}

    prompt = f"""
    Firmenname: {company['name']}
    Öffnungszeiten: {company['opening_hours']}
    Telefon: {company['phone']}
    Adresse: {company['address']}

    Wissen:
    {knowledge.get(company_id, '')}

    Kundenfrage:
    {question}
    """

    return {"answer": ask_llm(prompt)}
