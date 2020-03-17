from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
import pandas

# plot values
# x = [1, 2, 3, 4, 5]
# y = [3, 5, 6, 3, 1]

# read data from csv
df = pandas.read_csv("trees.csv")

# create ColumnDataSource from data
source = ColumnDataSource(df)

# generate the code on this file
output_file("index.html")

# get the value from source
tree_list = source.data["Tree"].tolist()

# add plot
p = figure(
    y_range = tree_list,
    plot_width = 800,           # width of the graph
    plot_height = 600,          # height of the graph
    title = "Trees Height",
    x_axis_label = "Height",
    tools="box_select,zoom_in,zoom_out,reset"       # set it to empty to remove the tools
)

# render graph
p.hbar(
    y = "Tree",
    right = "Height",
    left = 0,
    height = 0.4,               # height of the bar
    color="green",
    fill_alpha = 0.5,           # opacity
    source = source
)

# show results
save(p)           # save the file
# show(p)         # save the file and open a new tap