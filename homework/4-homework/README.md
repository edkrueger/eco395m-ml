# Homework 4 (10 Points + 3 Bonus)

In your private repo called `eco395m-ml-student` and invite the TA and I. Make a folder called `4-homework`. For exercises containing programming, take the starter code (if there is any) and move it into the folder and solve. For written exercises (including mathematical ones) either submit the solution as a neatly written scan or picture or a markdown file (containing LaTeX). Inside a file called `README.md` in the homework folder, indicate which file, images etc. contain which solutions.

1. **Log Targets and Tree/Forests**: In class, I argued that scaling of features does not make a difference to regression trees/forests. But, what happens when we transform the target? Let’s use Scikit-learn to explore using the hitters dataset.
   * a. (0 points) Load the hitters data, dropping the columns that are not numeric (we’ll look at how to encode categorical data later in the course) and the rows for which the salary is missing. The salary is the target.
   * b. (0 points) Split the dataset into a test and a train set using random_state=42
   * c. (0 points) Train a random forest regressor, with n_estimators=1000 to ensure stability.
   * d. (0 points) Train a transformed target regressor that utilizes a random forest with the same hyper parameters as above.
   * e. (3 points) For both models, calculate the MSE and the MAE, compare and discuss the results. Why does one model perform better for MSE and the other for MAE?
   * f. (1 points) Compute feature importances for both models. Which features are the most important in which models? Can you explain why?

2. **Out of Range Prediction and Tree-based Models**: (2 point) Using the random forest without transformation you trained in the last problem, make an out of range prediction for an observation $x$ where each feature's is greater than the max value of the features in `X_train`. Then make a prediction for $2 * x$ and $3 * x$. What do you observe? Can you explain it? What implications can you draw about the applicability of tree-based models extrapolation problems (i.e. timeseries)?

3. **Linear Regression with Coordinate Descent**: (4 Points) Implement Linear Regression with coordinate descent. When writing your tests, remember that coordinate descent produces the solution when the problem is convex, and, therefore should have the same parameter estimates as the closed form solution.


**Bonus**:

(3 Points) **LASSO**: Implement LASSO (linear regression with l1 penalty).  
Note that LASSO can be implemented simply be applying the soft thresholding operator to the coordinate-wise solution we did in class for linear regression.   
See slide 13 for Coordinate Descent on LASSO: https://www.stat.cmu.edu/~ryantibs/convexopt-S15/lectures/22-coord-desc.pdf   
See slide 20 for the soft thresholding operator: https://www.stat.cmu.edu/~ryantibs/convexopt-S15/lectures/06-subgradients.pdf