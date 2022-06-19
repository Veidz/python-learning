# Create a script that reads the width and height of a wall (meters) and calculates its area and amount of paint needed to paint it, knowing that each liter of paint paints an area of 2m².
wall_width = float(input('Enter the wall width: (m) '))
wall_height = float(input('Enter the wall height: (m) '))

wall_area = wall_width * wall_height

print('Wall area: {}m'.format(wall_area))
print('Amount of paint: {}l'.format(wall_area / 2))
