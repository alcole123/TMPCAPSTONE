import pytest
import requests


def prod_test():
    r=requests.get("http://54.164.17.201:8088/wp-json/wp/v2/posts")
    return r.status_code

def test_answer():
    assert prod_test() == 200

