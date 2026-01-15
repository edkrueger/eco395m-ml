# Homework 1 (10 Points + 3 Bonus)

Create a private repo called `eco395m-ml-student` and invite the TA and I. Make a folder called `1-homework`. For exercises containing programming, take the starter code (if there is any) and move it into the folder and solve. For written exercises (including mathematical ones) either submit the solution as a neatly written scan or picture or a markdown file (containing LaTeX). Inside a file called `README.md` in the homework folder, indicate which file, images etc. contain which solutions.

1. (2 points) **Solve for closed from coefficients in Univariate Linear Regression**: In class we solved univariate linear regression for $\beta_{0}$ in terms of $\beta_{1}$. Use this result and the first order conditions for $\beta_{1}$ to solve for $\beta_{0}$ and $\beta_{1}$ in terms of $x_{i}$ and $y_{i}$. Can you write this in terms of statistics operators/functions/variables?  
2. (1 point) Do ISL 3.7.5
3. (1 point) Do ISL 3.7.6
4. (1 point) **Negative R-Squared**: Give an example of a dataset and a model where R-Squared is negative. By hand, create a dataset containing three observations and make a model and show that R-squared is negative. Remember, a model is any function that maps an observations' feature to a predicted target.
5. **Simulation: Increasing Measurement Error R-squared**
    * a. (0 points) Create a feature vector with 1000 observations spaced evenly between 0 and 100. 
    * b. (1 point) Assume that the true relationship is $y^{*} = -1 + 3x$, but the target is measured with some error $\epsilon ~ N(0, \sigma^2)$. So, that $y_i = -1 + 3x_i + \epsilon$. For different values of $\sigma$, starting at 0 and going to 100 generate the target y, fit a linear model, and collect the r-squared, and coefficient estimates.
    * c. (1 point) Plot the r-squared values against $\sigma$.
    * d. (1 point) Do the coefficients differ for different $\sigma$? Does the R-squared differ across $\sigma$ values? In light of this simulation, give arguments that r-squared is and is not measuring "goodness of fit". What do you think?
6. **Simulation: R-squared for different Scales**
    * a. (0 points) This time, fix $\sigma = 2$ and assume that $y_i = -1 + 3x_i + \epsilon$ where $\epsilon ~ N(0, \sigma^2)$. Create two datasets, one with 1000 observations of x between 0 and 100 and another with x between 0 and 10.
    * b. (1 point) Fit a linear model for each dataset, record the coefficient and calculate the in-sample r-squared and MSE.
    * c. (1 point) Compare the models and their MSE and R-squared and discuss.
  
**Bonus**
(3 points) Do ISL 3.7.7
