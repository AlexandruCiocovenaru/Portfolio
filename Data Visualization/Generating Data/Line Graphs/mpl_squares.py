import matplotlib.pyplot as plt

# Generate the data.
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Style the plot
# plot_styles_available = plt.style.available
# print(plot_styles_available)
plt.style.use('seaborn')

# Set up the plot(s) in a figure plot collection.
fig, ax = plt.subplots()

# Plot data in a meaningful way - trend line
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# Display the plot in a figure plot collection.
plt.show()