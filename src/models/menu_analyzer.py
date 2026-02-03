def categorize_menu(df):
    """
    Categorizes items based on Profit and Popularity.
    """
    # 1. Group by Item Name to see how many sold and total profit
    menu_stats = df.groupby('item_name').agg({
        'quantity': 'sum',
        'item_profit': 'mean' # Assumes your data has a profit column
    })
    
    # 2. Find the average sales and average profit
    avg_sales = menu_stats['quantity'].mean()
    avg_profit = menu_stats['item_profit'].mean()
    
    # 3. Apply the 'Box' Logic
    def get_box(row):
        if row['quantity'] > avg_sales and row['item_profit'] > avg_profit:
            return "STAR (Keep & Promote)"
        elif row['quantity'] > avg_sales and row['item_profit'] <= avg_profit:
            return "PLOWHORSE (Raise Price)"
        elif row['quantity'] <= avg_sales and row['item_profit'] > avg_profit:
            return "PUZZLE (Better Marketing)"
        else:
            return "DOG (Remove from Menu)"

    menu_stats['category'] = menu_stats.apply(get_box, axis=1)
    return menu_stats
