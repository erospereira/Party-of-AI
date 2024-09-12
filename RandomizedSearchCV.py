from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor  # Import the DecisionTreeRegressor

# Example of hyperparameter tuning for a Decision Tree
param_grid = {'max_depth': [3, 5, 10], 'min_samples_split': [2, 5, 10]}
grid_search = GridSearchCV(DecisionTreeRegressor(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

# To view the best parameters found
print("Best parameters found:", grid_search.best_params_)

# To view the best model
best_model = grid_search.best_estimator_
print("Best model:", best_model)
