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

# Define columns to extract earlier
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

# Update output path to absolute path
output_path = Path(__file__).resolve().parent.parent / 'data' / 'processed' / 'lap_data.csv'
output_path.parent.mkdir(parents=True, exist_ok=True)

# Debug: Check if laps data is loaded
if laps.empty:
    print("No lap data found. Please check the session data.")
else:
    print(f"Loaded {len(laps)} laps.")

# Debug: Check if output path is valid
if not output_path.parent.exists():
    print(f"Output directory does not exist: {output_path.parent}")
else:
    print(f"Output directory is valid: {output_path.parent}")

# Save the data to a CSV file
lap_data = laps[cols]
lap_data.to_csv(output_path, index=False)

print("Lap data has been processed and saved to", output_path)