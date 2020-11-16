""" Script for plotting dataframes data. """

import constants
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def algorithm_execution_times(dataframe: pd.DataFrame, algorithms: list) -> None:
    """ Function to plot algorithm execution times in a lineplot. """
    for algorithm in algorithms:
        df = dataframe.query(f"{constants.INDEX_COL_FIRST} == '{algorithm}'")
        df = df.drop([constants.INDEX_COL_FIRST], axis=1)
        df.set_index(constants.INDEX_COL_SECOND, inplace=True)
        __plot_dataframe(identifier=algorithm, dataframe=df, plot_type="individual")


def cases_execution_times(dataframe: pd.DataFrame, cases: list) -> None:
    """ Function to plot cases execution times in a lineplot. """
    for case in cases:
        df = dataframe.drop([c for c in cases if c != case], axis=1)
        __plot_dataframe(identifier=case, dataframe=df, plot_type="grouped")


def __plot_dataframe(
    identifier: str, dataframe: pd.DataFrame, plot_type: str = "individual"
):
    ax = plt.axes(label=identifier)

    if plot_type == "individual":
        sns.lineplot(data=dataframe, marker="o", ax=ax)

    if plot_type == "grouped":
        sns.lineplot(
            data=dataframe,
            x=constants.INDEX_COL_SECOND,
            y=identifier,
            marker="o",
            ax=ax,
            hue=constants.INDEX_COL_FIRST,
        )

    ax.set_xlim(
        0,
    )
    ax.set_ylim(
        0,
    )
    ax.yaxis.grid(True)

    plt.ylabel("Tempo (segundos)")
    plt.xlabel("Quantidade de elementos do conjunto")
    plt.savefig(f"{constants.FIGURES_PATH}/{identifier}{constants.FIGURES_EXTENSION}")
