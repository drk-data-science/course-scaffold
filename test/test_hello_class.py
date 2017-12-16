import pytest
from hello_class import hello_class

def test_hello_class(capsys):
    hello_class()    
    out, err = capsys.readouterr()
    assert 'My Name is:' in out
    assert 'My Major is:' in out
    assert 'I attend:' in out
    assert 'My python version is:' in out
    assert 'It\'s nice to meet everyone.' in out
