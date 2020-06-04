
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def annotate_heatmap(im, data, format_string="{x:.2f}", text_params={}, symmetric=False,
        get_text_color = None):
    size_x = data.shape[0]
    size_y = data.shape[1]

    txt_formatter = matplotlib.ticker.StrMethodFormatter(format_string)
    txt_args = dict(horizontalalignment = "center", verticalalignment = "center")
    txt_args.update(text_params)

    for i in range(size_x):
        for j in range(size_y):
            if symmetric and j>i:
                txt_args["color"] = "white"
            elif get_text_color != None:
                txt_args["color"] = get_text_color(data[i][j])
            else:
                txt_args["color"] = "black"
            im.axes.text(j, i, txt_formatter(data[i, j], None), **txt_args)

# Creates an annotated heatmap from data
# 
# TODO: if matrix is symmetric, allow the choice of whether it should be upper
# or lower diagonal
# TODO: for now, the data is in RGB format and doesn't require a cmap
def heatmap(ax, data, row_labels, col_labels, symmetric=False, **kwargs):
    size_x = data.shape[0]
    size_y = data.shape[1]
    def_data = None

    if symmetric:
        # k=1 keeps the diagonal, maybe should be put in parameters?
        mask = np.triu(data, k=1)
        def_data = np.ma.array(data, mask=mask)
    else:
        def_data = data

    im = ax.imshow(def_data, **kwargs)
    ax.set_xticks(np.arange(size_x))
    ax.set_yticks(np.arange(size_y))
    ax.set_xticklabels(row_labels)
    ax.set_yticklabels(col_labels)

    ax.set_xticks(np.arange(data.shape[0])+1-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[1])+1-.5, minor=True)
    ax.tick_params(which="minor", bottom=False, left=False)

    plt.setp(ax.get_xticklabels(), rotation=45, rotation_mode="anchor", ha="right")

    ax.grid(which="minor", color="w", linestyle="-", linewidth=3)
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    return im
