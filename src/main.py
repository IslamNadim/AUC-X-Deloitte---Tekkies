import pandas as pd
import os

def load_and_merge_data():
    # 1. Define where the files are
    part1_path = 'data/fct_payments_part1.csv'
    part2_path = 'data/fct_payments_part2.csv'
    
    print("Loading data... please wait, these are large files!")
    
    # 2. Load the two pieces
    # We use 'low_memory=False' because the files are huge
    df1 = pd.read_csv(part1_path, low_memory=False)
    df2 = pd.read_csv(part2_path, low_memory=False)
    
    # 3. Glue them together
    full_df = pd.concat([df1, df2], ignore_index=True)
    
    print(f"Success! Total records loaded: {len(full_df)}")
    return full_df

if __name__ == "__main__":
    # This part runs when you start the program
    data = load_and_merge_data()
    
    # Show the first 5 rows to prove it works
    print(data.head())
