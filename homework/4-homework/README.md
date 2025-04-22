# Homework 4 (10 Points + 3 Bonus)

In your private repo called `eco395m-ml-student` and invite the TA and I. Make a folder called `4-homework`. For exercises containing programming, take the starter code (if there is any) and move it into the folder and solve. For written exercises (including mathematical ones) either submit the solution as a neatly written scan or picture or a markdown file (containing LaTeX). Inside a file called `README.md` in the homework folder, indicate which file, images etc. contain which solutions.

1. **Scikit-learn Random Forest**: (1 Points) In Scikit-Learn, does RandomForest use voting or average leaf probabilities?
2. **Pruned Decision Trees**: (2 Points) Implement a pruned decision tree with scikit-learn using the Caravan dataset. Evaluate the model and compare its performance to the models we used in class.
3. **ROC and Precision/Recall Curves**: (2 Points) Implement ROC and Precision-Recall Curves using only Python and, optionally, numpy. Show your results with matplotlib.
4. **AUC and Average Precision**: (2 Points) Implement ROC-AUC and average precision using your solution to the last problem.
5. **NLP**: (3 Points) I have held out 2000 observations for the economic new dataset in holdout.csv. Make the best possible modeling using the data you have used to make probability predictions for the positive class. Write these to a file called “{github_username}_predictions.csv” (i.e. for me the file will be called “edkrueger_predictions.csv”) with a column header of “proba”. We’ll evaluate your success using average precision (area under the precision/recall curve) and compare across the class. Submit your code as well.

**Bonus**:

**Stacking v.s. Ensemble in Random Forest**

(3 Points): Last class in a discussion with Matias, we considered the possibility of using a stacking estimator as the aggregation step in a Random Forest rather than voting or averaging class probabilities over trees. Implement this model by passing a list of copies of a DecisionTreeClassifier or ExtraTreeClassifier to StackingClassifier and use Logistic Regression as the final estimator. Investigate the performance across datasets. I hypothesize that performance will likely be similar to the Random Forest. However, probabilities from the model may be better calibrated because Logistic Regression tends to produce well calibrated probabilities and we use it as the final estimator (See https://scikit-learn.org/stable/modules/calibration.html). Investigate and discuss.
