
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# Creates an annotated heatmap from data
# 
# TODO: if matrix is symmetric, allow the choice of whether it should be upper
# or lower diagonal
def heatmap(ax, data, row_labels, col_labels, symmetric=False):

    im = ax.imshow(data)

    size_x = data.shape[0]
    size_y = data.shape[1]

    ax.set_xticks(np.arange(size_x))
    ax.set_yticks(np.arange(size_y))
    ax.set_xticklabels(row_labels)
    ax.set_yticklabels(col_labels)

    ax.set_xticks(np.arange(data.shape[0])+1-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[1])+1-.5, minor=True)
    ax.tick_params(which="minor", bottom=False, left=False)

    plt.setp(ax.get_xticklabels(), rotation=45, rotation_mode="anchor", ha="right")

    txt_formatter = matplotlib.ticker.StrMethodFormatter("{x:.2f}")
    txt_args = dict(horizontalalignment = "center", verticalalignment = "center")

    ax.grid(which="minor", color="w", linestyle="-", linewidth=3)
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    for i in range(size_x):
        for j in range(size_y):
            im.axes.text(j, i, txt_formatter(data[i, j], None), txt_args)

    return im
