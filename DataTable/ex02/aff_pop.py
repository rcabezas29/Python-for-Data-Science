import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def shorthand_to_number(s):
    """
    Substitute string numbers with shorthands to numeric values
    """
    if 'k' in s:
        return float(s.replace('k', '')) * 1_000
    elif 'M' in s:
        return float(s.replace('M', '')) * 1_000_000
    else:
        return float(s)


def main():
    """
    
    """
    df = load("../dfs/population_total.csv")


    spain = df.loc[df['country'] == 'Spain']
    spain_data = [shorthand_to_number(x) for x in spain.iloc[0, 1:].to_numpy()]
    france = df.loc[df['country'] == 'France']
    france_data = [shorthand_to_number(x) for x in france.iloc[0, 1:].to_numpy()]

    plt.plot(np.asarray(france.columns[1:]), france_data, color='b', label='France')
    plt.plot(np.asarray(spain.columns[1:]), spain_data, color='g', label='Spain')
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.legend(loc='lower right')
    plt.xticks(ticks=[str(x) for x in np.arange(1800, 2081, 40)])
    plt.yticks(ticks=[x for x in np.arange(20_000_000, 61_000_000, 20_000_000)], labels=['20M', '40M', '60M'])
    plt.ylabel('Population')
    plt.show()


if __name__ == "__main__":
    main()
