import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '712c3f7837286ec7588ea32798abd7ea'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "generate",
    "photo_id": "-1"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_data = response_create.json()
pokemon_id = response_data.get("id")

body_name = {
    "pokemon_id": pokemon_id,
    "name": "Mimi",
    "photo_id": 2
}

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)

body_pokeball = {
    "pokemon_id": pokemon_id
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)