# Homework 3 (10 Points + 3 Bonus)

In your private repo called `eco395m-ml-student` and invite the TA and I. Make a folder called `3-homework`. For exercises containing programming, take the starter code (if there is any) and move it into the folder and solve. For written exercises (including mathematical ones) either submit the solution as a neatly written scan or picture or a markdown file (containing LaTeX). Inside a file called `README.md` in the homework folder, indicate which file, images etc. contain which solutions.

1. **Logistic Regression**: (1 Points) Scikit-learn's Logistic Regression, with the default parameters, doesn’t match other packages/implementations. In particular, by default, the objective function is slightly different from standard logistic regression. How? What option can you change to get the standard behavior?
2. **Balanced Accuracy is Accuracy on Balanced Dataset**: (2 Points) Show that Balanced Accuracy=(1/2)(recall + specificity) reduces to Accuracy if the classes are balanced for a binary classification problem.
3. **Balanced Accuracy is Accuracy After Balancing**: (3 Points) Show that reweighting the 0-class observations (TN, FP) by the imbalance and computing accuracy is equivalent to Balanced Accuracy=(1/2)(recall + specificity) for a binary classification problem.
4. **Linear Regression with Coordinate Descent**: (4 Points) Implement Linear Regression with coordinate descent. When writing your tests, remember that coordinate descent produces the solution when the problem is convex, and, therefore should have the same parameter estimates as the closed form solution.

**Bonus**:

(3 Points) **LASSO**: Implement LASSO (linear regression with l1 penalty).  
Note that LASSO can be implemented simply be applying the soft thresholding operator to the coordinate-wise solution we did in class for linear regression.   
See slide 13 for Coordinate Descent on LASSO: https://www.stat.cmu.edu/~ryantibs/convexopt-S15/lectures/22-coord-desc.pdf   
See slide 20 for the soft thresholding operator: https://www.stat.cmu.edu/~ryantibs/convexopt-S15/lectures/06-subgradients.pdf

