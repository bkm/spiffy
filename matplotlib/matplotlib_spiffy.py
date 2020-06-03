
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def heatmap(ax, data, row_labels, col_labels):

    im = ax.imshow(data)

    ax.set_xticks(np.arange(data.shape[0]))
    ax.set_yticks(np.arange(data.shape[1]))
    ax.set_xticklabels(row_labels)
    ax.set_yticklabels(col_labels)

    ax.grid(which="minor", color="w", linestyle="-", linewidth=3)

    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    return im
