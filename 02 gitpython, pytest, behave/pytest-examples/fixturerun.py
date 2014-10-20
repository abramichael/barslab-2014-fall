

from pytest import fixture

@fixture
def context_data():
	class SuperBuperData:
		a = 5
		def f(self):
			pass
		def g(self):
			return False

	return SuperBuperData()

def test_superbuperdata(context_data):
	assert context_data.a == 5
	assert not(context_data.g())
