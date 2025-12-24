from fastapi import FastAPI
from app.data import companies, knowledge
from app.llm import ask_llm

app = FastAPI()

@app.get("/")
def root():
    return {"status": "kundenAssistent läuft ✅"}

@app.get("/chat")
def chat(company_id: str, question: str):
    company = companies.get(company_id)

    if not company:
        return {"answer": "Firma nicht gefunden."}

    context = f"""
    Du bist der kundenAssistent für {company['name']}.

    Adresse: {company['address']}
    Telefon: {company['phone']}
    E-Mail: {company['email']}
    Öffnungszeiten: {company['opening_hours']}
    Leistungen: {company['services']}

    {knowledge}
    """

    answer = ask_llm(question, context)
    return {"answer": answer}
