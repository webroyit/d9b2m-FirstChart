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
    y_range = tree,
    plot_width = 800,           # width of the graph
    plot_height = 600,          # height of the graph
    title = "Trees Height",
    x_axis_label = "Height",
    tools=""                    # set it to empty to remove the tools
)

# render graph
p.hbar(
    y = tree,
    right = h,
    left = 0,
    height = 0.4,               # height of the bar
    color="green",
    fill_alpha = 0.5            # opacity
)

# show results
show(p)