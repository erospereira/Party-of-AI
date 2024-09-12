# Feature Engineering Example
demographics_df['population_growth_rate'] = demographics_df['population'].pct_change().fillna(0)
economics_df['normalized_income'] = (economics_df['income'] - economics_df['income'].mean()) / economics_df['income'].std()
