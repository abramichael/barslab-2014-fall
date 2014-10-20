from behave import *
from player import Player

@given(u'a new player')
def step_impl(context):
    context.p = Player("A")
    assert context.p is not None

@then('HP should be 100')
def step_impl(context):
    assert context.p.hp == 100

@then(u'he should have name')
def step_impl(context):
    assert context.p.name is not None

@then(u'he can do the kick')
def step_impl(context):
    assert context.p.kick is not None

@given(u'two players')
def step_impl(context):
    context.p = Player('a')
    context.p2 = Player('b')

@when(u'first kicks second on {d}')
def step_impl(context,d):
    context.hp2 = context.p2.hp
    context.p.kick(context.p2, int(d))

@then(u'second\'s HP is decreasing to {d}')
def step_impl(context,d):
    assert context.hp2 - context.p2.hp == int(d)
