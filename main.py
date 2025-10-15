from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# --- Modelo de datos ---
class Concept(BaseModel):
    id: int
    name: str
    definition: str
    book_section: str

# --- Base inicial de conceptos ---
concepts = [
    {
        "id": 1,
        "name": "Lean Startup",
        "definition": "Metodología que aplica los principios del pensamiento lean al emprendimiento, reduciendo desperdicio y aprendiendo rápido del cliente.",
        "book_section": "Las raíces del Lean Startup"
    },
    {
        "id": 2,
        "name": "Aprendizaje Validado",
        "definition": "Proceso de comprobar con datos reales qué funciona y qué no en un producto, para aprender del cliente y mejorar decisiones.",
        "book_section": "Las raíces del Lean Startup"
    },
    {
        "id": 3,
        "name": "Motor de Crecimiento",
        "definition": "Mecanismo interno que impulsa el progreso de una startup mediante la mejora continua del producto, marketing y operaciones.",
        "book_section": "El motor del crecimiento"
    },
    {
        "id": 4,
        "name": "Ciclo Construir–Medir–Aprender",
        "definition": "Bucle de retroalimentación donde los emprendedores construyen, miden resultados y aprenden para decidir si seguir o cambiar.",
        "book_section": "Dirección y aprendizaje"
    },
    {
        "id": 5,
        "name": "Visión de la Startup",
        "definition": "Destino final y propósito que guía las decisiones estratégicas y el desarrollo del negocio.",
        "book_section": "Visión y estrategia"
    },
    {
        "id": 6,
        "name": "Gestión Empresarial en Startups",
        "definition": "Enfoque gerencial adaptado a la incertidumbre de las nuevas empresas, combinando creatividad y disciplina.",
        "book_section": "Gestión Empresarial"
    },
    {
        "id": 7,
        "name": "Pivotar (Cambio de rumbo)",
        "definition": "Cambio estratégico basado en el aprendizaje validado, sin abandonar la visión general de la startup.",
        "book_section": "Dirección y aprendizaje"
    }
]

# --- Crear aplicación FastAPI ---
app = FastAPI(title="Lean Startup API", version="1.0")

# --- Rutas CRUD ---

@app.get("/concepts", response_model=List[Concept])
def get_concepts():
    return concepts

@app.get("/concepts/{concept_id}", response_model=Concept)
def get_concept(concept_id: int):
    for c in concepts:
        if c["id"] == concept_id:
            return c
    raise HTTPException(status_code=404, detail="Concept not found")

@app.post("/concepts", response_model=Concept)
def create_concept(concept: Concept):
    if any(c["id"] == concept.id for c in concepts):
        raise HTTPException(status_code=400, detail="ID already exists")
    concepts.append(concept.dict())
    return concept

@app.put("/concepts/{concept_id}", response_model=Concept)
def update_concept(concept_id: int, updated_concept: Concept):
    for i, c in enumerate(concepts):
        if c["id"] == concept_id:
            concepts[i] = updated_concept.dict()
            return updated_concept
    raise HTTPException(status_code=404, detail="Concept not found")

@app.delete("/concepts/{concept_id}")
def delete_concept(concept_id: int):
    for i, c in enumerate(concepts):
        if c["id"] == concept_id:
            del concepts[i]
            return {"message": f"Concept {concept_id} deleted"}
    raise HTTPException(status_code=404, detail="Concept not found")
