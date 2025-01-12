import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def generate_data(points_count: int) -> pd.DataFrame:
    min_X, max_X = 0.0, 25.0

    X = min_X + np.random.rand(points_count) * max_X
    Y = X + 0.25 * X * np.sin(0.025 * X * X + X)

    data = {
        "X": X,
        "Y": Y
    }

    return pd.DataFrame(data)


def visualize_v1(data: pd.DataFrame) -> None:
    plt.scatter(
        data.X, 
        data.Y, 
        s=3,            # marker size
        c=data.Y,  # values for cmap
        cmap='viridis'  # options : viridis, plasma, inferno, magma, cividis, seismic, coolwarm, tab10
    )

    plt.show()

def visualize_v2(data: pd.DataFrame) -> None:
    plt.style.use('ggplot')

    label_font = {
        'family': 'serif',
        'color': 'darkblue',
        'size': 10
    }

    plt.xlabel('X-axis label', fontdict=label_font)
    plt.ylabel('Y-axis label', fontdict=label_font)
    plt.title('Example of Scatter Plot')

    plt.scatter(
        data.X, 
        data.Y, 
        s=3,            # marker size
        c=data.Y,  # values for cmap
        cmap='viridis'  # options : viridis, plasma, inferno, magma, cividis, seismic, coolwarm, tab10
    )

    plt.axvline(18, color='r', linestyle='dashed', linewidth=1)
    plt.axvline(22, color='b', linestyle='dashed', linewidth=1)

    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    print(f"Pandas version : {pd.__version__}")

    pd_data = generate_data(1000)
    visualize_v2(pd_data)

    print("Success")