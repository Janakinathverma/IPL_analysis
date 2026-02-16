-- 1️⃣ Total Matches Played
SELECT COUNT(DISTINCT match_id) AS total_matches
FROM ipl;

-- 2️⃣ Matches Per Season
SELECT season, COUNT(DISTINCT match_id) AS matches_played
FROM ipl
GROUP BY season
ORDER BY season;

-- 3️⃣ Top 5 Teams by Wins
SELECT winner, COUNT(*) AS wins
FROM ipl
WHERE winner IS NOT NULL
GROUP BY winner
ORDER BY wins DESC
LIMIT 5;

-- 4️⃣ Toss Impact
SELECT 
    ROUND(
        SUM(CASE WHEN toss_winner = winner THEN 1 ELSE 0 END) * 100.0 
        / COUNT(*), 2
    ) AS toss_win_percentage
FROM ipl;

-- 5️⃣ Top 5 Venues by Matches
SELECT venue, COUNT(*) AS matches
FROM ipl
GROUP BY venue
ORDER BY matches DESC
LIMIT 5;

-- 6️⃣ Player of the Match Count
SELECT player_of_match, COUNT(*) AS awards
FROM ipl
GROUP BY player_of_match
ORDER BY awards DESC
LIMIT 5;
