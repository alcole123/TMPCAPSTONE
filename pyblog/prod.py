import pytest
import requests


def prod_test():
    r=requests.get("http://54.164.17.201:8088/wp-json/wp/v2/posts")
    s=r.status_code
    return s



def prod_test_2():
    r=requests.get("http://54.164.17.201:8088/wp-json/wp/v2/posts")
    js=r.json()
    t=" "
    for i,data in enumerate(js):
        t=js[i]['id']
        return t


t=prod_test_2()
print(t)

def test_answer():
    assert prod_test() == 200

def test_answer2():
    assert prod_test_2() == 13