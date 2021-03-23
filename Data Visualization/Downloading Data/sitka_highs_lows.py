import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f) # read the file
    header_row = next(reader) # return the next line in the file
    # print(header_row)

    # return both CSV index of each item and the CSV value of each item in the list header_row
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # get dates, high and low temperatures from the CSV file
    dates, highs, lows = [], [], []
    for row in reader: # reader object continues from where it left off above, returning each line
        # loop through each line, pulling data from index 2 (DATE) and index 5 (TMAX), convert them to date obj and int
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Style the plot
plt.style.use('seaborn')

# Set up the plot(s) in a figure plot collection
fig, ax = plt.subplots()

# Plot data in a meaningful way - trend lines
ax.plot(dates, highs, c='red', alpha=0.5) # alpha arg controls transparency (alpha=1 -> completely opaque)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2) # facecolor arg used for the in between region

# Set chart title and label axes.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # draw date labels diagonally, prevent overlapping
plt.ylabel("Temperature (F)", fontsize=16)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=16)

# Display the plot in a figure plot collection.
plt.show()
