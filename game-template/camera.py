from engine import *

# Define a Camera class
class Camera:

# Inside the Camera class, create an __init__ method
  def __init__(self, pos=[0, 0]):
# - Initialize a position attribute with a default value of [0, 0]
# - Initialize a velocity attribute for horizontal movement (vx) with a value of 0

  def move(self, player):
# Create a move method in the Camera class that accepts a player object as an argument
# - Update the camera's horizontal position based on its velocity and a time delta (dt)
# - Check if the player's x-coordinate is within a certain range (hint: between 200-16 and 600-16)
#   - If the player collides with an obstacle on the left or right, stop the camera's movement
#   - Otherwise, set the camera's velocity to match the player's velocity
# - Add bounds to the camera's position:
#   - If the camera moves past the left boundary (position < 0), reset it to 0 and stop its movement
#   - If the camera moves past the right boundary (position > 400), reset it to 400 and stop its movement
