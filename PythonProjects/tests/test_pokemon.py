import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '712c3f7837286ec7588ea32798abd7ea'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 33870

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_name():
    response_get = requests.get(url = f'{URL}/trainers/{TRAINER_ID}', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["trainer_name"] == 'Баба Капа'
