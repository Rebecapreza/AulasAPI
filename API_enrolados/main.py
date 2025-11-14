from fastapi import FastAPI, HTTPException, status, Response, Depends
from models import personagensEnrolados, personagemEnrolados, personagem
from typing import Dict

app = FastAPI(title= "API Enrolados - DS18", version="0.0.1", description="Feita por Rebeca Preza")

personagens: Dict[int, personagem] = {
    1:{
        "nome": "Rapunzel",
        "personalidade": "princesa perdida",
        "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSA1u23Ux4xv13MwAMFPs6k5eBzSNM5KejuRlshXFD9HhKblJ_8J8DySmGNb7RsjNB6oD8&usqp=CAU"
    },
    2:{
        "nome": "Flynn Rider",
        "personalidade": "bandido caçado",
        "foto": "https://pbs.twimg.com/media/EPEtR9EWkAAicRk.jpg"
    }, 
    3:{
        "nome": "Pascal",
        "personalidade": "camaleão de estimação",
        "foto": "https://i.pinimg.com/736x/ec/29/e8/ec29e8edb8f59a94d69d5a67ccc8337f.jpg"
    },
    4:{
        "nome": "Maximus",
        "personalidade": "cavalo branco que ajuda na fuga",
        "foto": "https://i.pinimg.com/736x/e1/a4/7f/e1a47fd626e2bba2cff9b188e3d9b25e.jpg"
    },
    5:{
        "nome": "Mamãe Gothel",
        "personalidade": "Bruxa que abusa dos poderes da rapunzel pra não envelhecer",
        "foto": "https://i.pinimg.com/736x/24/c7/61/24c7616ae6994266eaa56167166d2e5b.jpg"
    }
}

@app.get("/personagens")
async def get_personagens():
    return list (personagens.values())

@app.get("/personagens/{personagem_id}")
async def buscar_personagem(personagem_id: int):
    personagem = personagens.get(personagem_id)
    if not personagem:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")
    return personagem

@app.post("/personagens", status_code=status.HTTP_201_CREATED)
async def criar_personagem(personagem: personagem):
    next_id = max(personagens.keys(), default=0) + 1
    novo_personagem = personagem(id=next_id, **personagem.dict())
    personagens[next_id] = novo_personagem
    return novo_personagem

@app.put("/personagens/{personagem_id}")
async def atualizar_personagem(personagem_id: int, personagem: personagem):
    if personagem_id not in personagens:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")
    atualizado = personagem(id=personagem_id, **personagem.dict())
    personagens[personagem_id] = atualizado
    return atualizado

@app.delete("/personagens/{personagem_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_personagem(personagem_id: int):
    if personagem_id not in personagens:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")
    del personagens[personagem_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8001, log_level="info", reload=True)