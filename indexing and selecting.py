import pandas as pd

# Data load
df = pd.read_csv(r"C:\Users\Admin\Downloads\ipl_2024_deliveries.csv")

# Specific columns select panrathu
selected_data = df[['batting_team', 'bowling_team', 'striker', 'bowler', 'runs_of_bat']]

# Extra: Rows edukkudhu where 'runs_of_bat' > 4
high_runs_data = df[df['runs_of_bat'] > 4]

# Columns index use panni oru particular row-a select pannalam
row_data = df.iloc[10]  # 10th row

# Save to CSV
selected_data.to_csv('selected_data.csv', index=False)
high_runs_data.to_csv('high_runs_data.csv', index=False)
