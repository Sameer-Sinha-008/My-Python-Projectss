class GameCharacter:
    def __init__(self, health):
        self._health = health
    @property
    
    def health(self):
        return self._health
    
    @health.setter
    def health(self, new_health):
           if new_health > 100:
               self._health = 100
            
           elif new_health < 0:
               self._health = 0
           else:
               self._health = new_health
player = GameCharacter(1)
player.health = 192
print(player.health)
