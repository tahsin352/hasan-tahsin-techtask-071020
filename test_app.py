import requests

def test_app():
    url = 'http://127.0.0.1:5000/lunch'
    resp = requests.get(url)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"
    
    resp_body = resp.json()
    assert len(resp_body["recipes"]) == 3
    assert resp_body["recipes"][0]["title"] == "Fry-up"
    assert resp_body["recipes"][2]["title"] == "Salad"