import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Loads 2 datasets and displays a scatter plot to represent the
    relation between GDP and the life expectancy in 1900
    """
    df1 = load(
        '../dfs/income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
        )
    df2 = load('../dfs/life_expectancy_years.csv')

    incomes = df1['1900']
    le = df2['1900']

    plt.scatter(incomes, le)
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life expectancy')
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.show()


if __name__ == "__main__":
    main()
