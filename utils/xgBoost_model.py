from xgboost import XGBClassifier
from imblearn.pipeline import Pipeline, make_pipeline
from imblearn.over_sampling import SMOTE
from sklearn.metrics import make_scorer, f1_score
from sklearn.model_selection import GridSearchCV


# ---------------------------------------------------------------- #

# Make pipeline
classifier = XGBClassifier()
pipeline = make_pipeline(SMOTE(), classifier)


# Set parameters values for grid
param_grid = {
    "xgbclassifier__learning_rate":[0.01, 0.3, 0.5],
    "xgbclassifier__n_estimators": [10, 100, 200],
    "xgbclassifier__max_depth": [1, 3, 5],
    "xgbclassifier__objective": ["binary:logistic"],
    "xgbclassifier__use_label_encoder": [False],
    "xgbclassifier__booster": ["gbtree"],
    "xgbclassifier__eval_metric": ["logloss"]}

# Make custom scoring metric
scorer = make_scorer(f1_score, pos_label=1)

# Intantiate GridSearchCV
grid_search_cv = GridSearchCV(pipeline, param_grid, scoring = scorer)