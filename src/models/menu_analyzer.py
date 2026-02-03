import pandas as pd

def categorize_menu(df):
    """
    Categorizes items based on Profit and Popularity.
    """
    # 1. Group by Item Name to see total sales and average profit
    # (Note: Check your CSV column names. Replace 'item_name' if it's named differently)
    menu_stats = df.groupby('item_name').agg({
        'quantity': 'sum',
        'item_profit': 'mean' 
    })
    
    # 2. Find the average sales and average profit to create our 'crosshair'
    avg_sales = menu_stats['quantity'].mean()
    avg_profit = menu_stats['item_profit'].mean()
    
    # 3. Apply the 'Box' Logic (The Matrix)
    def get_box(row):
        if row['quantity'] > avg_sales and row['item_profit'] > avg_profit:
            return "STAR"
        elif row['quantity'] > avg_sales and row['item_profit'] <= avg_profit:
            return "PLOWHORSE"
        elif row['quantity'] <= avg_sales and row['item_profit'] > avg_profit:
            return "PUZZLE"
        else:
            return "DOG"

    menu_stats['category'] = menu_stats.apply(get_box, axis=1)
    return menu_stats
