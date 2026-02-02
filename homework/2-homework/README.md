# Homework 2 (10 Points)

Create a private repo called `eco395m-ml-student` and invite the TA and I. Make a folder called `2-homework`. For exercises containing programming, take the starter code (if there is any) and move it into the folder and solve. For written exercises (including mathematical ones) either submit the solution as a neatly written scan or picture or a markdown file (containing LaTeX). Inside a file called `README.md` in the homework folder, indicate which file, images etc. contain which solutions. Use only Python and Numpy for this HW.

1. **Implement OOP Triangles**: In `homework/2-homework/triangles` there is a file called `base_triangle.py` containing a base class of triangles called `BaseTriangle`. In `oop_triangles.py` you will implement `IsoscelesTriangle` and `RightTriangle` which both inherit from `BaseTriangle`. You should be able to do so without overriding any methods inherited from `BaseTriangle`. You'll know your code work when it passes the assertions made in `if __name__ == "__main__"` block of the code. Do not modify the assertions.
    * a. (1 point) Finish implementing IsoscelesTriangle.
    * b. (1 point) Implement RightTriangle.
      
2. **Implement KNN**: In `homework/2-homework/diy_regressor/knn.py` you'll implement KNN is the style of a scikit-learn regressor. You can test your implementation by running the code and seeing if the assertions under `if __name__ == "__main__"` pass. You can also calculate the MSE against a real dataset. Do not modify the assertions in `knn.py`.
    * a. (3 points) Implement KNN
    * b. (1 point) When running against the advertising dataset (in `main_diy.py`) what effect does changing k have? What k is results in the lower MSE?

4. **Implement Distance-Weighted KNN**: In class, we suggested an alternative algorithm for KNN: instead of predicting an average of the targets for the k-closest observations to the input observation, predict a weighted average of the targets according to the inverse distance between their observations and the input observation.
   * a. (3 points) Add an optional parameter to the `KNeighborsRegressor` constructor called `weighted`. When `weighted=True` use the alternative algorithm, otherwise use the standard one. Show that your code works by adding additional assertions.
   * b. (1 points) Compare this version of the algorithm to the standard version for the advertising data by modifying the code in `main_diy.py`. What are your findings? When and why might this algorithm be better than the standard algorithm?
