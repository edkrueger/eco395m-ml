# Homework 3 (10 Points + 3 Bonus)

In your private repo called `eco395m-ml-student` and invite the TA and I. Make a folder called `3-homework`. For exercises containing programming, take the starter code (if there is any) and move it into the folder and solve. For written exercises (including mathematical ones) either submit the solution as a neatly written scan or picture or a markdown file (containing LaTeX). Inside a file called `README.md` in the homework folder, indicate which file, images etc. contain which solutions.

1. **Polynomial Regression Optimal Degree**: (1 points) In class, we looked at polynomial regression with 0, 2 and very large degree polynomial features. Using Scikit-learn (GridSearchCV and make_pipeline, etc.), on the advertising dataset, determine what degree is optimal. Show the degree, the train MSE and the test MSE.
   
2. **Out of Range Predictions for Linear Models**: (2 points) Using the advertising dataset, take linear regression, the pipeline we trained for the log-log model in class and the polynomical pipeline from the previous exercise and train the models. Make an out of range prediction for an observation $x$ where each feature's is greater than the max value of the features in `X_train`. Then make a prediction for $2 * x$ and $3 * x$. What do you observe? Can you explain it? What implications can you draw about the applicability of of these models to out of range predictions?

3. **Tree Depth**: (1 point) Assuming no irreducible error in the dataset (i.e. there are no two observations that have the same feature values, but different target values), for a dataset of length N, what is the depth of the regression tree that will be formed with scikit-learn default hyperparameters?

4. **Optimal Split**: (3 points) Implement a function called optimal_split that takes a feature matrix X and a target y and returns the optimal split (the index of the feature and the value at which the split occurs), i.e. the split that minimizes MSE. Write tests ( assert statements) that show that your function works. One of your tests should show that your algorithm works on a feature matrix with one feature, another should work on a feature matrix of two features. Your function should extend to arbitrarily many features.

5. **Decision Tree**: (3 points) Implement a decision tree in the style of Scikit-learn (fit/predict methods) using only Python, the standard library, numpy or scipy. For convenience, you may assume that there is no irreducible error in the dataset (i.e. there are no two observations that have the same feature values, but different target values). You may also implement the algorithm so that every terminal node has exactly one observation in it. Write tests to show that your model is working. If your dataset doesn’t have irreducible error, your train MSE should be 0. (Hint: One approach to this problem is to implement a recursive function, another approach is to use a while-loop. In either case, you’ll likely want to use optimal_split as a helper function and perhaps modify it to also return the right and left datasets.)

**Bonus**:

(3 Points) **Piecewise Linear Regression Tree**: (3 points) For a region in the regression tree, for each partition, we fit the average of the point $y_i$ partition where $x_i$ was in the partition: $\hat{y}_{R_j}$ = avg( $y_i : x_i \in R_j)$. 

Consider instead, fitting linear regression in each partition: in each partition fit linear regression for obsevations $i : x_i \in R_j$ to compute $\hat{y}_{R_j}$ and using these estimators both in evaluating split and in the final model.

Implement this model in the style of Scikit-learn (fit/predict methods) using only Python, the standard library, numpy or scipy. You may start with your work in the previous exercise, but should implement a hyperparameter that limits the maximum splits by terminating the algorithm early called `max_splits`. Write tests to show that your model is working.
