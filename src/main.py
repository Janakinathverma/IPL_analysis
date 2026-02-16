import os
import pandas as pd
from data_cleaning import clean_data
from analysis import (
    total_matches_played,
    matches_per_season,
    top_teams_by_wins,
    toss_impact
)
from visualisation import plot_matches_per_season, plot_top_teams
from utils import print_section, percentage_format


def main():
    try:
        # Ensure output directories exist
        os.makedirs("outputs/plots", exist_ok=True)
        os.makedirs("outputs/reports", exist_ok=True)

        # Load data
        df = pd.read_csv("data/IPL.csv", low_memory=False)

        # Clean data
        df = clean_data(df)

        # ======================
        # 📊 Analysis Section
        # ======================

        print_section("Total Matches")
        total = total_matches_played(df)
        print(total)

        print_section("Matches Per Season")
        season_data = matches_per_season(df)
        print(season_data)

        print_section("Top Teams")
        top_teams = top_teams_by_wins(df)
        print(top_teams)

        print_section("Toss Impact")
        impact = toss_impact(df)
        print(percentage_format(impact))

        # ======================
        # 📈 Visualization
        # ======================

        plot_matches_per_season(season_data)
        plot_top_teams(top_teams)

        # ======================
        # 💾 Save Reports
        # ======================

        season_data.to_csv("outputs/reports/matches_per_season.csv", index=False)
        top_teams.to_csv("outputs/reports/top_teams.csv", index=False)

        print_section("Process Completed Successfully ✅")

    except Exception as e:
        print("Error occurred:", e)


if __name__ == "__main__":
    main()
