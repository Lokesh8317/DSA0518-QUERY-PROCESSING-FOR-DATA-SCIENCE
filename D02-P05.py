import pandas as pd
import numpy as np
data = {
    'ord_no': [np.nan, np.nan, 70002.0, np.nan, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, np.nan],
    'purch_amt': [np.nan, 270.65, 65.26, np.nan, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, np.nan],
    'ordr_date': [np.nan, "2012-10-06", np.nan, np.nan, "2012-10-08", "2012-10-09", "2012-10-22", "2012-10-10",
                  "2012-10-15", "2012-10-21", "2012-10-16", np.nan],
    'cust_id': [np.nan, 3001, 3001, np.nan, 3002, 3001, 3001, 3004, 3003, 3002, 3001, np.nan]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
rows_with_two_or_more_nan = df[df.isna().sum(axis=1) >= 2]
print("\nRows with at least 2 NaN values:")
print(rows_with_two_or_more_nan)           