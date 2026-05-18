import pandas as pd
import sqlite3

skater_stats = pd.read_csv("C:/Users/Jake/Desktop/game_skater_stats.csv")
goalie_stats = pd.read_csv("C:/Users/Jake/Desktop/game_goalie_stats.csv")
player_info = pd.read_csv("C:/Users/Jake/Desktop/player_info.csv")

print("--- TOP SCORERS ---")
top_scorers = skater_stats.groupby("player_id").agg({"goals": "sum", "assists": "sum"}).sort_values("goals", ascending=False)
print(top_scorers.head(10))

merged_scorers=pd.merge(top_scorers, player_info, on="player_id")
print(merged_scorers[["firstName", "lastName", "goals", "assists"]].head(10))

top_goalies= goalie_stats.groupby("player_id").agg({"savePercentage" : "mean", "game_id" : "count"}).sort_values("savePercentage", ascending=False) 

merged_goalies=pd.merge(top_goalies, player_info, on="player_id") 

merged_goalies = merged_goalies[merged_goalies["game_id"] > 70]
print(merged_goalies[["firstName", "lastName", "savePercentage", "game_id"]].head(10))

nationality_counts = player_info.groupby("nationality")["player_id"].count().sort_values(ascending=False)  
print(nationality_counts.head(10))

merged_scorers.head(10).to_csv("C:/Users/Jake/Desktop/top_scorers.csv", index=False)
merged_goalies.head(10).to_csv("C:/Users/Jake/Desktop/top_goalies.csv", index=False)
nationality_counts.head(10).reset_index().to_csv("C:/Users/Jake/Desktop/nationality_NHL.csv", index=False)

print(goalie_stats["game_id"].min(), goalie_stats["game_id"].max())