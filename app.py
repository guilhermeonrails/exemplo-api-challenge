from fastapi import FastAPI
from models.review import Review
from controller.reviews import ler_reviews, escrever_nova_review

app = FastAPI()

@app.get("/")
def root():
    '''Função root do projeto de API da live do challenge.'''
    return {"Fast":"API"}

@app.get("/{name}")
def say_hello(name: str):
    if not name:
        pass
    return {"oi": name}

@app.get("/api/reviews")
def get_reviews():
    return ler_reviews()

@app.post("/api/reviews")
def create_review(review: Review):
    reviews = ler_reviews()
    reviews.append(review.model_dump())
    escrever_nova_review(reviews)
    return review
