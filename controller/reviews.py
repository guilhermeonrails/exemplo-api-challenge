import json

def ler_reviews():
    with open("data/reviews.json", "r") as file:
        return json.load(file)

def escrever_nova_review(data):
    with open("data/reviews.json", "w") as file:
        json.dump(data, file, indent=2)