from app import app
from fastapi.testclient import TestClient
client = TestClient(app)
def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello i give bmi'}

def test_underweight():
    payload = {"weight":50,"height":1.80} 
    response = client.post('/obesity',json = payload)
    assert response.status_code  == 200
    assert response.json() == {'status': 'underweight'}

def test_healthy():
    payload = {'weight':68,'height':1.75}
    response = client.post('/obesity',json= payload)
    assert response.status_code ==   200
    assert response.json() == {'status':'healthy'}

def test_overweight():
    payload = {'weight':90,'height':1.80}
    response = client.post('/obesity',json=payload)
    assert response.status_code == 200
    assert response.json() == {'status':'overweight'}
    


