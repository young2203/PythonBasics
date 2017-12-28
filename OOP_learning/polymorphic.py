# This is an example of showing polymorphic property of python
# both super class Card and its subclasses will share the same
# method: _points() , all of the subclasses share the same signature,
# same method and same attributes. The objects of these three subclasses
# could be used alternatively within one script

class Card:
    def __init__(self, rank, suit ) :
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()
        
class NumberCard(Card) :
    def _points(self) :
        return int(self.rank), int(self.rank)
        
class AceCard(Card):
    def _points(self):
        return 1, 11
        
class FaceCard(Card) :
    def _points(self):
        return 10, 10
        
myCards = [AceCard('A','?'), NumberCard('2','?'), NumberCard('3','?')]
print myCards
