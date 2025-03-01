Knight class mod:

def move(self, tiles, enemies):
	— rest of code as usual
    # **Check collision with enemies** !!! This bit here is the change
    for enemy in enemies:
        if self.rect.colliderect(enemy.rect):
            self.handle_enemy_collision(enemy)

New method: 
def handle_enemy_collision(self, enemy):
    if self.down_attack:  
        enemy.destroy()  
        self.vy = -20  # Bounce off the enemy
    else:
        print("Player hit!")  


Beet class mod:
def destroy(self):
    # add logic here for destroying

But now when you move the knight it has to have the following:
knight.move(tiles, enemies)
