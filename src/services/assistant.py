from collections import defaultdict


def generate_menu_insights(clustered_items):
    """
    Takes clustered menu data and returns
    human-readable business insights + recommendations.
    """

    categories = defaultdict(list)

    # Group items by menu engineering category
    for item in clustered_items:
        cat = item.get("menu_category", "Unknown")
        categories[cat].append(item)

    insights = []

    # ---- Stars ----
    if "Star" in categories:
        insights.append(
            "⭐ Stars are high-profit and high-demand items. "
            "Keep pricing stable and highlight them in promotions."
        )

    # ---- Plowhorses ----
    if "Plowhorse" in categories:
        insights.append(
            "🐎 Plowhorses sell well but have lower margins. "
            "Consider small price increases or cost optimization."
        )

    # ---- Puzzles ----
    if "Puzzle" in categories:
        insights.append(
            "🧩 Puzzles have high margins but low demand. "
            "Improve descriptions, placement, or marketing visibility."
        )

    # ---- Dogs ----
    if "Dog" in categories:
        insights.append(
            "🐶 Dogs perform poorly in both demand and profit. "
            "Consider removing or redesigning these items."
        )

    # ---- Overall summary ----
    insights.append(
        "📊 Menu engineering analysis completed. "
        "Focus on promoting Stars, optimizing Plowhorses, marketing Puzzles, "
        "and eliminating Dogs to maximize profitability."
    )

    return {
        "summary": "AI-generated menu insights based on clustering analysis.",
        "insights": insights,
        "total_items": len(clustered_items),
        "category_counts": {k: len(v) for k, v in categories.items()},
    }