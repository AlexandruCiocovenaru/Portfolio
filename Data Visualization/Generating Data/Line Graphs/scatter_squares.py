import matplotlib.pyplot as plt

# Generate the data.
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# Style the plot.
plt.style.use('seaborn')

# Set up the plot(s) in a figure plot collection.
fig, ax = plt.subplots()

# Plot data in a meaningful way - single point (colored)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.get_cmap('Blues'), s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Save fig to file before displaying.
plt.savefig('squares_plot.png', bbox_inches='tight')

# Display the plot in a figure plot collection.
plt.show()