# ==================================
# IPL CRICKET ANALYSIS PROJECT
# ==================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
# ==================================
# CREATE OUTPUT FOLDER
# ==================================
if not os.path.exists("output"):
  os.makedirs("output")  
# ==================================  
# LOAD DATASETS
# ==================================
print("Loading datasets.......")
matches=pd.read_csv(r"C:\Users\kalya\OneDrive\Desktop\dataset\matches.csv")
# print(matches)
deliveries=pd.read_csv(r"C:\Users\kalya\OneDrive\Desktop\dataset\deliveries.csv")
# print(deliveries)
print("Datasets loaded Successfully!")
# ==================================
# BASIC INFORMATION
# ==================================
print("\nMatches Dataset shape:")
print(matches. shape)
print("\nDeliveries Dataset shape:")
print(deliveries. shape)
# ==================================
# DATA CLEANING
# ==================================
matches.drop_duplicates(inplace=True)
deliveries.drop_duplicates(inplace=True)
print(matches.isnull().sum())
# ==================================
# TOTAL MATCHES
# ==================================
total_matches=matches.shape[0]
print("\nTotal IPL Matches:", total_matches)
# ==================================
# TEAM WINSS ANALYSIS
# ==================================
team_wins=matches['winner'].value_counts()
print("\nTop Winning Teams:")
print(team_wins.head(10))

plt.figure(figsize=(12,6))

sns.barplot(
  x=team_wins.head(10).values,
  y=team_wins.head(10).index
)
plt.title("Top 10 IPL Teams by Wins")
plt.xlabel("Win")
plt.ylabel("Team")
plt.tight_layout()
plt.savefig("output/team_wins.png")
plt.show()
# =============================
# TOP BATSMEN
# =============================
top_batsmens=(
  deliveries.groupby('batter')['batsman_runs']
  .sum()
  .sort_values(ascending=False)
  .head(10)
)
print("\nTop 10 Run Scores:")
print(top_batsmens)
plt.figure(figsize=(12,6))
sns.barplot(
  x=top_batsmens.values,
  y=top_batsmens.index
)
plt.title("Top 10 Run Scorers in IPL")
plt.tight_layout()
plt.savefig("output/top_batsmen.png")
plt.show()
# ==============================
# TOP BOWLERS
# ==============================
wickets=deliveries[
  deliveries['is_wicket']==1
]
top_bowlers=(
  wickets.groupby('bowler')['is_wicket']
  .count()
  .sort_values(ascending=False)
  .head(10)
)
print("\nTop 10 Wicket Takers:")
print(top_bowlers)
plt.figure(figsize=(12,6))
sns.barplot(
  x=top_bowlers.values,
  y=top_bowlers.index
)
plt.title("Top 10 Wicket Takers")
plt.tight_layout()
plt.savefig("output/top_bowler.png")
plt.show()
# =============================
# VENUE ANALYSIS
# =============================
venue_analysis=matches['venue'].value_counts().head(10)
print("\nTop Venues:")
print(venue_analysis)
plt.figure(figsize=(12,6))
sns.barplot(
  x=venue_analysis.values,
  y=venue_analysis.index
)

plt.title("Top IPL Venues")
plt.tight_layout()
plt.savefig("output/top_venues.png")
plt.show()
# ===============================
# PLAYER OF MATCH ANALYSIS
# ===============================
pom=matches['player_of_match'].value_counts().head(10)
print("\nMost Player of Match Awards:")
print(pom)
plt.figure(figsize=(12,6))
sns.barplot(
  x=pom.values,
  y=pom.index
)
plt.title("Most Player of match Awards")
plt.tight_layout()
plt.savefig("output/player_of_match.png")
plt.show()
# ===============================
# TOSS TMPACT ANALYSIS
# ===============================
toss_match=matches[
  matches['toss_winner']==
  matches['winner']
]
percentage=(
  len(toss_match)
  /
  len(matches)
)*100
print(
  f"\nToss Winner Won Match:{percentage:2f}%"
)
# ===============================
# ORANGE CAP ANALYSIS
# ===============================
orange_cap=(
  deliveries.groupby("batter")
  ['batsman_runs']
  .sum()
  .sort_values(ascending=False)
  .head(10)
)
print("\nOrange Cap Leaderboard")
print(orange_cap)
# ==============================
# PURPLE CAP ANALYSIS
# ==============================
purple_cap=(
  wickets.groupby("bowler")
  ['is_wicket']
  .count()
  .sort_values(ascending=False)
  .head(10)
)
print("\nPurple Cap Leaderboard")
print(purple_cap)
# ==============================
# TEAM RUNS ANALYSIS
# ==============================
team_runs=(
  deliveries.groupby('batting_team')
  ['total_runs']
  .sum()
  .sort_values(ascending=False)
)
print("\nTeam Runs:")
print(team_runs.head())
plt.figure(figsize=(12,6))
sns.barplot(
 x=team_runs.head(10).values,
 y=team_runs.head(10).index
)
plt.title("Top Teams by Runs")
plt.tight_layout()
plt.savefig("output/team_runs.png")
plt.show()
# ====================================
# YEAR WISE MATCHES
# ====================================
if 'season' in matches.columns:
  year_matches=matches['season'].value_counts()
  plt.figure(figsize=(12,6))
  sns.barplot(
    x=year_matches.index,
    y=year_matches.values
  )
  plt.title("Matches Per Season")
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.savefig("output/year_matches.png")
  plt.show()
  
# ========================================
# EXPORT REPORT
# =======================================
report=pd.DataFrame({
  "Metric":[
    "Total Matches",
    "Teams",
    "Players",
    "Venues"
    ],
  "Value":[
    matches.shape[0],
    matches['winner'].nunique(),
    deliveries['batter'].nunique(),
    matches['venue'].nunique()
  ]
})
report.to_excel(
  "output/IPL_Report.xlsx",
  index=False
)
# ===================================
# FINAL INSIGHTS
# ===================================
print("\n==============================")
print("IPL BUSINESS INSIGHTS")
print("=================================")
print(
  "Most Sucessful Team:",
  team_wins.idxmax()
)

print(
  "Highest Run Scorer:",
  orange_cap.idxmax()
)

print(
  "Highest Wicket Taker:",
  purple_cap.idxmax()
)

print(
  "Most Used Venue:",
  venue_analysis.idxmax()
)
print("\n PROJECT COMPLETED SUCCESSFULLY!")
print("All Report Saved in OUTPUT Folder")