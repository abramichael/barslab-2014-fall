from utils.matem import fact
import pytest

def test_fact():
	assert fact(1) == 1
	assert fact(2) == 2
	assert fact(5) == 120

def test_fact_negative():
	with pytest.raises(ValueError):
		n = fact(-1)

def test_fact_is_int():
	with pytest.raises(TypeError):
		n = fact(2.5)
	with pytest.raises(TypeError):
		n = fact("abc")