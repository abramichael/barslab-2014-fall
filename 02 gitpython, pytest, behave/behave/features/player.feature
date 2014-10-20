Feature: HP managing
  
  Scenario: HP on the game starting
  	Given a new player
  	Then HP should be 100
  	and he should have name
  	and he can do the kick

  Scenario: kicking
  	Given two players 
  	When first kicks second on 20
  	Then second's HP is decreasing to 10