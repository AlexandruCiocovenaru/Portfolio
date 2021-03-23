import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making random walks, as long as the program is active
while True:
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Style the random walk
    plt.style.use('classic')

    # Set up the plot(s) in a figure plot collection (with figsize parameter in inches and dpi resolution).
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

    # Plot data in a meaningful way - single point (colored points, without outline)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values,
               c=point_numbers, cmap=plt.cm.get_cmap('Blues'),
               edgecolors='none', s=1)

    # Emphasize the first and last points in the walk.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    # Display the plot in a figure plot collection.
    plt.show()

    keep_running = input("Make another walk? (y/n) ")
    if keep_running == 'n':
        break
