
class card():
    def __init__(self, values, suit):
        self.values = values      
        self.suits = suit          
        self.name = values + " of " + suit  


my_card = card("Ace", "Spades")
   

print(my_card.suits)
print(my_card.name)

