import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def main():
    """
    Open a CSV to transform it to a life epectancy x year plot
    """
    df = load("../dfs/life_expectancy_years.csv")
    try:
        row = df.loc[df['country'] == 'Spain']
        plt.plot(np.asanyarray(row.columns[1:]), row.iloc[0, 1:].to_numpy())
        plt.title('Spain life expectancy Projections')
        plt.xlabel('Year')
        plt.xticks(ticks=[str(x) for x in np.arange(1800, 2081, 40)])
        plt.ylabel('Life expectancy')
        plt.show()
    except Exception:
        print("Unable to show the plot")
        return


if __name__ == "__main__":
    main()
