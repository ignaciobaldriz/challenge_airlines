from scipy.stats import uniform
from imblearn.pipeline import Pipeline, make_pipeline
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression, RandomizedSearchCV

# ----------------------------------------------------- #


def logReg_model1():

    # Create regularization penalty space
    penalty = ['l2']

    # Create regularization hyperparameter distribution using uniform distribution
    C = uniform(loc=0, scale=4)

    # Create hyperparameter options
    hyperparameters = dict(C=C, penalty=penalty)

    # instantiate the model (using the default parameters)
    logreg = LogisticRegression(random_state=16)

    logreg_cv = RandomizedSearchCV(logreg, hyperparameters, random_state= 16, cv = 5) # generate a log reg and test in 5 folders the best params of the grid

    return logreg_cv



def logReg_model2():

    pipeline = Pipeline(steps = [['smote', SMOTE(random_state=11)],
                                    #['scaler', MinMaxScaler()],
                                    ['classifier', LogisticRegression(random_state=11,
                                                                    max_iter=1000)]])


    param_grid = {'classifier__C':[0.001, 0.01, 0.1, 1, 10, 100, 1000]}

    grid_search = GridSearchCV(estimator=pipeline,
                            param_grid=param_grid,
                            scoring='recall',
                            cv=5,
                            n_jobs=-1)

    return grid_search
