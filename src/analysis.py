import pandas as pd


def total_matches_played(df):
    """
    Return total unique matches played.
    Works for ball-by-ball dataset.
    """
    if 'match_id' in df.columns:
        return df['match_id'].nunique()

    raise ValueError("Column 'match_id' not found.")


def matches_per_season(df):
    """
    Return number of matches played per season.
    """
    if {'season', 'match_id'}.issubset(df.columns):
        return (
            df.groupby('season')['match_id']
            .nunique()
            .reset_index(name='matches_played')
            .sort_values('season')
        )

    raise ValueError("Required columns missing: 'season' or 'match_id'.")


def top_teams_by_wins(df):
    """
    Return top 5 teams with most wins.
    Handles ball-by-ball dataset correctly.
    """
    if {'match_id', 'match_won_by'}.issubset(df.columns):

        # Reduce to one row per match
        match_level = (
            df[['match_id', 'match_won_by']]
            .drop_duplicates()
            .dropna()
        )

        return (
            match_level['match_won_by']
            .value_counts()
            .head(5)
            .reset_index()
            .rename(columns={'index': 'team', 'match_won_by': 'wins'})
        )

    raise ValueError("Required columns missing: 'match_id' or 'match_won_by'.")


def toss_impact(df):
    """
    Calculate percentage of matches where toss winner
    also won the match.
    """

    if {'match_id', 'toss_winner', 'match_won_by'}.issubset(df.columns):

        # Reduce to match level
        match_level = (
            df[['match_id', 'toss_winner', 'match_won_by']]
            .drop_duplicates()
            .dropna()
        )

        impact = (
            (match_level['toss_winner'] == match_level['match_won_by'])
            .mean()
            * 100
        )

        return round(impact, 2)

    raise ValueError("Required columns missing: 'match_id', 'toss_winner', or 'match_won_by'.")
