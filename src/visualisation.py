import matplotlib.pyplot as plt

def plot_matches_per_season(df):
    """
    Bar chart of matches per season
    Expects DataFrame with columns:
    ['season', 'matches_played']
    """
    plt.figure()
    df.set_index('season')['matches_played'].plot(kind='bar')
    plt.title("Matches Per Season")
    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.tight_layout()
    plt.show()


def plot_top_teams(df):
    """
    Bar chart of top winning teams
    Expects DataFrame with columns:
    ['winner', 'wins']
    """
    plt.figure()
    df.set_index('winner')['wins'].plot(kind='bar')
    plt.title("Top 5 Teams by Wins")
    plt.xlabel("Team")
    plt.ylabel("Wins")
    plt.tight_layout()
    plt.show()
