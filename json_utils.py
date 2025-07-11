import json

def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
        
def salvar_tarefas(lista):
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        return json.dump(lista, arquivo, indent=2, ensure_ascii=False)