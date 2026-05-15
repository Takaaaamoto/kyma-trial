from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok", "message": "動いてます"}

@app.get("/skills/{employee_id}")
def get_skills(employee_id: str):
    return {"employee_id": employee_id, "skills": ["SAP CPI", "Python"]}