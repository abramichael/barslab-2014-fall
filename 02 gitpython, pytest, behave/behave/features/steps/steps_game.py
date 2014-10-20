from game import Game
from behave import *

@given(u'a new game')
def step_impl(context):
    context.game = Game()

@then(u'it should have 2 players')
def step_impl(context):
    assert context.game.player1 is not None
    assert context.game.player2 is not None