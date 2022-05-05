import requests, pytest



r=requests.get('http://127.0.0.1:8050/')
t=r.text

def test_existence_header():
    assert '<head>' in t


def test_regionPicker():
    assert 'react-entry-point' in t

def test_visPresence():
    assert '_dash-loading' in t    