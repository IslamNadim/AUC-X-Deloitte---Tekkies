import pandas as pd
# IMPORTANT: This line 'imports' your logic from the other folder
from models.menu_analyzer import categorize_menu 

def load_and_merge_data():
    part1_path = 'data/fct_payments_part1.csv'
    part2_path = 'data/fct_payments_part2.csv'
    print("Loading data... please wait!")
    df1 = pd.read_csv(part1_path, low_memory=False)
    df2 = pd.read_csv(part2_path, low_memory=False)
    full_df = pd.concat([df1, df2], ignore_index=True)
    return full_df

if __name__ == "__main__":
    # STEP 1: Load the data
    data = load_and_merge_data()
    
    # STEP 2: Run the analysis (Calling the code from the other file)
    print("Analyzing menu performance...")
    results = categorize_menu(data)
    
    # STEP 3: Show the results
    print("\n--- MENU ENGINEERING RESULTS ---")
    print(results.head(10)) # Shows the first 10 items and their category
