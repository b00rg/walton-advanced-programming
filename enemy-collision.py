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


def update(self):
    knight = None
    enemies = []

    # Categorize entities into player and enemies
    for entity in self.level.entities:
        if isinstance(entity, Knight):
            knight = entity  # Identify the player
        elif isinstance(entity, Beeto):
            enemies.append(entity)  # Store enemies in a list

    # Ensure we have a knight before updating
    if knight:
        knight.move(self.level.tiles, enemies)  # Pass enemies for collision

    # Update all entities
    for entity in self.level.entities:
        entity.update(self.level.tiles)

    # Move camera to follow the knight
    if knight:
        self.camera.move(knight)
