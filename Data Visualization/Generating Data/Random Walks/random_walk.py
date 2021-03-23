from random import choice


class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1]) # go left (1) or right (-1)
            x_distance = choice([0, 1, 2, 3, 4]) # choose how far in steps
            x_step = x_direction * x_distance # determine the length of each step

            y_direction = choice([1, -1]) # go up (1) or down (-1)
            y_distance = choice([0, 1, 2, 3, 4]) # choose how far in steps
            y_step = y_direction * y_distance # determine the length of each step

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue # if the walk stays in the same place, ignore and move on

            # Calculate the new position.
            x = self.x_values[-1] + x_step # add x_step value to the last value stored in x_values
            y = self.y_values[-1] + y_step # add y_step value to the last value stored in y_values

            self.x_values.append(x)
            self.y_values.append(y)