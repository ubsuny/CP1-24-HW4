"""
This generates a CSV file with information on 22 nebulae, organized
into 9 groups based on their velocity and distance.

Data:
    - Group: Group number assigned to each nebula (1–9).
    - Nebula: Name or ID of the nebula (e.g., NGC 278).
    - Velocity (km/sec): Radial velocity of each nebula in km/sec.
    - Distance (parsecs): Distance of each nebula from Earth in parsecs.

Output:
    The CSV file 'hubble_9_groups.csv' is created in the current
    directory, containing the above information.

Usage:
    Run this script directly to generate the CSV file.
"""
import pandas as pd

# data to include all 22 nebulae
data = {
    "Group": [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 9, 9],
    "Nebula": ["NGC 278", "NGC 404", "NGC 584", "NGC 936", "NGC 1023", "NGC 1700", "NGC 2681", "NGC 2683",
               "NGC 2841", "NGC 3034", "NGC 3368", "NGC 3379", "NGC 3623", "NGC 4111", "NGC 4526", "NGC 4565",
               "NGC 5866", "NGC 3521", "NGC 4954", "NGC 3115", "NGC 4826", "NGC 7331"],
    "Velocity (km/sec)": [650, -25, 1800, 1300, 300, 800, 700, 400, 600, 290, 940, 810, 800, 800, 580, 1100, 650, 730, 1200, 920, 150, 500],
    "Distance (parsecs)": [1.52, 1.52, 3.45, 2.37, 0.62, 1.16, 1.42, 0.67, 1.24, 0.79, 1.74, 1.49, 1.79, 1.20, 2.35, 2.23, 1.73, 1.27, 2.10, 1.00, 0.9, 1.1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV file
csv_file_path = 'hubble_9_grouping.csv'
df.to_csv(csv_file_path, index=False)

print(f"CSV file saved at: {csv_file_path}")
