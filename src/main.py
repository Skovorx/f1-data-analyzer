import fastf1
import pandas as pd
from pathlib import Path

# Enable cache for FastF1
cache_path = Path(__file__).resolve().parent.parent / 'cache'
cache_path.mkdir(parents=True, exist_ok=True)  # Ensure the cache directory exists
fastf1.Cache.enable_cache(str(cache_path))

# Load session data
session = fastf1.get_session(2024, 'Monza', 'R')
session.load()

# Extract lap data
laps = session.laps

# Define columns to extract
cols = [
    'Driver',
    'Team',
    'LapNumber',
    'LapTime',
    'Stint',
    'Compound',
    'TyreLife',
    'Position'
]

# Create a DataFrame with the selected columns
lap_data = laps[cols]

# Save the data to a CSV file
output_path = Path('../data/processed/lap_data.csv')
output_path.parent.mkdir(parents=True, exist_ok=True)
lap_data.to_csv(output_path, index=False)

print("Lap data has been processed and saved to", output_path)