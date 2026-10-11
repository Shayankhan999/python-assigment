-- Step 1: Data Load Ho Raha Hy ---
Shuru mein Rows: 8631, Columns: 17

--- Step 2: Data Ka Audit ---
Missing values har column mein:
 Invoice ID                  0
Branch                      0
City                        0
Customer type              64
Gender                      0
Product line                0
Unit price                  0
Quantity                    0
Tax 5%                      0
Total                       0
Date                       17
Time                        0
Payment                     0
cogs                        0
gross margin percentage     0
gross income                0
Rating                     88
dtype: int64

Exact duplicate rows ki tadad: 30
Duplicate Invoice IDs ki tadad: 55
Gender columns ki unique values: <StringArray>
['Female', 'Male', ' Female', 'MALE ', 'male', 'female']
Length: 6, dtype: str
Payment columns ki unique values: <StringArray>
['Ewallet', 'Credit card', 'Cash', 'cash', ' Credit card', 'ewallet ',
 'EWALLET']
Length: 7, dtype: str
--- Step 3: Exact Duplicate Rows Ko Delete Karna ---
Rows bache: 8601
--- Step 4: Duplicate Invoice IDs Theek Karna ---
Rows bache: 8576
--- Step 5: Text Columns Ko Standardise Karna ---
Text cleaning mukammal!

--- Step 6: Negative Quantities Ko Positive Karna ---
Quantities theek ho gayin!

--- Step 7: Mixed Dates Ko Format Karna ---
Dates parse ho gayin!
