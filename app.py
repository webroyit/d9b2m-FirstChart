from bokeh.plotting import figure, output_file, show
import pandas

# plot values
# x = [1, 2, 3, 4, 5]
# y = [3, 5, 6, 3, 1]

# read data from csv
df = pandas.read_csv("trees.csv")

tree = df["Tree"]
h = df["Height"]

# generate the code on this file
output_file("index.html")

# add plot
p = figure(
    title = "First Graph",
    x_axis_label = "X Axis",
    y_axis_label = "Y Axis"
)

# render line graph
p.line(x, y, legend="Test", line_width = 2)

# show results
show(p)