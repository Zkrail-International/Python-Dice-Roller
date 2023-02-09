import random as r

class d:
  
  def roll(least,sides):
    result = r.randrange(1,(sides+1))
    return result
  
  def aroll(least,sides,amount,modifier):
    
    base = 1
    result = 0
    
    for base in range(amount):
      roll = d.roll(least,sides)
      result += roll
    result = (result+modifier)
    return result
'''
1 is the least you can roll. 20 is the sides the virtual dice has. 
3 is how many times it is rolled, it automatically adds the rolls together. 
0 is what you add to the roll after it has been rolled
'''
variable = d.aroll(1,20,3,0)
print(variable)