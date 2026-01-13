# Final Project

## Introduction

You’ll work in self-assigned groups with 3-5 members. (If there are too many small groups, I may have to merge them or adjust presentation times. I'm potentially open to groups of 6, but it is important to check with me and demonstrate that your scope will have enough work so that every member can contribute.)

You’ll pick a problem that you’d like to apply classfication to and then pick a dataset that helps you solve that problem. You’ll try different techniques to solve the problem and evaluate their results, strengths and weaknesses and make a recommendation for the best model for your problem.


### The Problem

Your problem should be primarily a prediction problem. You should do some inference and investigation to inspire your modeling approach, explain how your models work and reveal which features have the most influence over the models and their predictions.

Your problem may be an application of predictive modeling to a subject matter (applied project), or it may be an investigation of a statistical/ML technique, objectives, etc (theory project).

Some example of problems might be:
* Building a model to predict how likely a person will purchase a good.
* Building a model to predict wheter a loan application will be approved. You’ll need to discuss regulations when deciding on the best model.
* Investigating techniques, metrics, etc. useful in training and evaluating models for specific criteria or goal (i.e. time-series, post-hoc fairness, explainability, class-imbalance, etc.). This will be like a literature review with code demonstrating and evaluating the different techniques against a dataset.
* Replicating an inference paper, but evaluating its models and others for predictive accuracy. Your choice of best model will balance interpretability with predictive accuracy.
* Replicating a prediction paper, but with new techniques and data.

If you are doing an applied project, make sure that you understand the subject matter well enough to understand what real world problem your model will solve and communicate this in your presentation and README.md.

If you are doing a theory project, make sure you can explain the problem you are trying to investigate in your README.md and presentation and provide evidence for your evaluations.

### The Data

For an applied project, make sure that the dataset is real (i.e. no synthetic data) and that you understand how the data was collected, by whom and for what purpose and what weaknesses it might have. You may also collect your own data (most likely through web scraping, but possibly through a survey or experiment), in this case document its collection.

If you cannot find a dataset with clear lineage or collect one for your problem, you should select a different problem.

For a theory project, your data may not need to be as clear of a lineage, but understand if your data is synthetic and make sure that you understand and explain its features with respect to your problem. You may want to use more than one dataset. You may also create your own synthetic data for exploration, if the creation process is reproducible and documented.


### The Deliverables

You’ll produce a README.md which will explain your problem, explain and present relevant analysis of your dataset, show the results of evaluating your models, detailing your modeling process and your final conclusion.

You’ll include an appendix that explains how to use your code to create your results. You must provide your code and README.md in a public GitHub repo. 

## Use of a New Models, Techniques or Packages  - (10 points)
* You'll use at least one model, technique or package that we did not cover in class.

## The Report in README.md - (25 points)

The report should cover your problem, data sources and your evaluation and your recommendations.  

Requirements for reporting your modeling and evaluation:
* The problem must be clearly articulated and goals must be clear
* Source(s) of dataset(s) must be clearly documented
* Data collection methods must be understood and clearly documented. You should read and summarize the documentation of the data, make sure that you understand and document all columns/features that are relevant to your analysis. You should understand and summarize what isn’t in the data too.
* Limitations of the data must be clearly outlined
* Your modeling approaches must be clearly explained and evaluated.
* The limitations of the modeling must be clearly outlined.
* You must make recommendations for the best model or approach
* You should not include analysis, plots, discoveries, that aren’t directly related to your findings – you can put them as an appendix in another file if you like

## Reproducibility - (10 points)

Your work must be reproducible. This means that anyone should be able to follow your instructions to run your code on your data and get the same results you do.  

Requirements for reproducibility:
* Instructions to rerun that analysis must be included in the README.md
* Additional packages should be included in `requirements.txt`
* All data cleaning must be reproducible through code – data must not be manually modified (i.e. no modifications in Excel)
* Must use relative paths
* Data should be included in the repository if the dataset is small enough, otherwise, instructions for downloading the datasets and placing them in the right locations are required
* Your code should have as few entry points as reasonable. I.e. rather than requiring `data_cleaning_step_1.py`, `data_cleaning_step_2.py`, etc., to be run, have simply `data_cleaning.py`

## Code Quality - (25 points)

Requirements for formatting:
* Your code should use double and single quotes consistently
* Long lines, pipes or method chains must be broken into smaller lines
* (Note: Formatting can be automated using [black](https://black.readthedocs.io/en/stable/) for .py files or [nb-black](https://pypi.org/project/nb-black/) for notebooks)

Requirements for clean code:
* You should remove unused imports
* You should delete functions that are no longer used
* You should remove code that isn’t used
* You should not have any commented out code

Requirements for comments and docstrings:
* Functions should have simple docstrings explaining their inputs and outputs
* Comments should be used sparingly either to clarify difficult to understand, unintuitive or otherwise surprising code or to add structure (Note: In most cases, a function with a docstring will be a better option than a comment)

Software design:
* Use appropriate tools for appropriate tasks, don't use tools when you don't need them (i.e. don't use Pandas dataframes as an unnecessary replacement for dictionaries and lists)
* Use tools appropriately (i.e. use method chaining in Pandas)
* Consistency in the use of tools (i.e. using just one graphing library or visualization tool with consistent styling)
* Use of functions to produce modular code
* Use for pipelines, ColumnTransformer and other scikit-learn abstractions

Security:
* You won't leak credentials (you _really_ do not want to do this in a public repo, but you shouldn't do it in a private one either -- ask me why)

## Repo - (5 points)

Requirements for the repo:
* Your group must collaborate in a single repository
* When you submit your project, all of your code and documentation should be on the main branch
* You should use GitHub Issues to organize your work and allow for collaboration
* You should make a branch for each issue
* Your repo should have at least 60 commits as a group

## Presentation - (5 points)

Requirements for the presentation:
* You should try to test your setup in BRB 1.118 before the day of presentations if possible, problems during the setup will cut into your presentations and affect your grade.
* The presentation must be around 10 minutes (subject to number of groups) – we’ll cut you off if it isn’t.
* The presentation should primarily focus on your goal, methodology, findings, limitations and potential extensions.
* You should limit your discussion of packages or techniques, whether related to the code or otherwise, to things that your classmates would not already know either from in class or in their training as Economists.
* Your whole group should collaborate in designing and rehearsing the presentation. With additional time, I recommend having more than one member speak, but it is acceptable if one person wishes to take the presentation.
* You’ll have 5 minutes of Q&A with the class and me.

## Individual Requirements - (20 points)
* You must solve at least four meaningful issues and the code must be merged into the main branch.
* You make at least 10 meaningful commits and the code must be merged into the main branch.
* You must attend your group’s presentation and all others
* Declaration of work.


