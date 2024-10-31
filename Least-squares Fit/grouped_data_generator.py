"""
This module processes data from Table 1 of Hubble's 1929 article. This data is located
in this directory by the name of 'raw_data_table1_grouped.md' which was prepared by
iglesias-cardinale (github ID: 112112966). This module calculates grouped averages
and uncertainties, and saves the results to a CSV file for further analysis.

Main steps:
1. Import required libraries.
2. Load and extract relevant columns (OBJECT, r, and v) from raw data.
3. Apply group labels based on predefined groups.
4. Calculate mean values and uncertainties for each group.
5. Filter out rows with undefined uncertainties and save the final processed data to CSV.
"""

import pandas as pd
import numpy as np

# Read the data and extract relevant columns
file_path_grouped = 'Least-squares Fit/raw_data_table1_grouped.md'
data_grouped = pd.read_csv(file_path_grouped, delim_whitespace=True)

# Extract OBJECT, r, and v columns and apply group labels
object_r_v_columns_grouped = data_grouped[['OBJECT', 'r', 'v']]
group_labels = {
    "'S.Mag.'": 'Group 1', "'L.Mag.'": 'Group 1',
    '598': 'Group 2', '221': 'Group 2', '224': 'Group 2',
    '1068': 'Group 3',
    '3627': 'Group 4', '3031': 'Group 4',
    '4258': 'Group 5', '4151': 'Group 5', '4382': 'Group 5', '4472': 'Group 5',
    '4486': 'Group 5', '4649': 'Group 5', '4449': 'Group 5', '4214': 'Group 5',
    '4826': 'Group 5', '4736': 'Group 5',
    '5236': 'Group 6', '5055': 'Group 6', '5457': 'Group 6', '5194': 'Group 6',
    "'N.G.C.6822'": 'Group 7',
    '7331': 'Group 8'
}
object_r_v_columns_grouped['Group'] = object_r_v_columns_grouped['OBJECT'].map(group_labels)

# Calculate mean r, v, and uncertainty of v for each group without filtering
group_means = object_r_v_columns_grouped.groupby('Group')[['r', 'v']].mean()
group_std = object_r_v_columns_grouped.groupby('Group')['v'].std()
group_size = object_r_v_columns_grouped.groupby('Group')['v'].count()
group_uncertainty_v = group_std / np.sqrt(group_size)

# Create the initial unfiltered data table
group_summary_unfiltered = pd.DataFrame({
    'x': group_means['r'],
    'y': group_means['v'],
    'sigma': group_uncertainty_v
}).reset_index()

# Apply filtering to remove rows with NaN in 'sigma' and create filtered data table
group_summary_filtered = group_summary_unfiltered.dropna(subset=['sigma'])

# Save the filtered data to CSV file
output_path_filtered = 'Least-squares Fit/grouped_data_filtered.csv'
group_summary_filtered.to_csv(output_path_filtered, index=False)
