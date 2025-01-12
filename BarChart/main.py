import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

from matplotlib import colors


def visualize(values: np.array, bins: int) -> None:
    plt.style.use('ggplot')
    plt.figure(figsize=(12, 10), dpi=80)


    # Draw hist
    N, bins, patches = plt.hist(
        values,
        bins=bins,
        color='skyblue',
        edgecolor='black'
    )

    # Setting colors
    fracs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.max() / 2, fracs.max())

    for curr_frac, curr_patch in zip(fracs, patches):
        #color = plt.cm.viridis(norm(curr_frac))
        color = plt.cm.winter(norm(curr_frac))

        curr_patch.set_facecolor(color)

    # Draw labels
    label_font = {
        'family': 'serif',
        'color': 'darkblue',
        'size': 14
    }

    plt.xlabel("Values", fontdict=label_font, labelpad=15)
    plt.ylabel("Frequency", fontdict=label_font, labelpad=15)
    plt.title("Histogram example")
    plt.ticklabel_format(axis='both', style='plain')

    plt.xticks(np.arange(0, 210, 10))

    plt.show()


def generate(count: int) -> np.array:
    #min_value, max_value = 1.0, 1000.0
    #values = np.random.uniform(min_value, max_value, size=(count,))

    loc, scale = 100, 10
    values = np.random.normal(loc, scale, size=(count,))

    return values


if __name__ == "__main__":
    print(f"Pandas version : {pd.__version__}")

    values_count = 1000
    bins_count = 25

    values = generate(values_count)
    visualize(values, bins_count)

    print("Success")
