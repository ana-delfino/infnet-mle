"""
This is a boilerplate pipeline 'Treinamento'
generated using Kedro 0.19.12
"""
import pandas as pd
from pycaret.classification import ClassificationExperiment
from sklearn.metrics import f1_score, log_loss

def log_reg_model_train(x_train, y_train, session_id, n_iter=50):
    exp = ClassificationExperiment()
    exp.setup(data=x_train, target=y_train['shot_made_flag'] , session_id=session_id, silent=True, log_experiment=True)

    lr_model = exp.create_model('lr')
    tuned_lr = exp.tune_model(
        lr_model, 
        n_iter=n_iter, 
        optimize='F1', 
        search_library="optuna", 
        search_algorithm="tpe", 
        early_stopping=True
    )
    return tuned_lr

def decision_tree_model_train(x_train, y_train, session_id, n_iter=50):

    exp = ClassificationExperiment()
    exp.setup(data=x_train, target=y_train['shot_made_flag'],  session_id=session_id, silent=True, log_experiment=True)

    dt_model = exp.create_model('dt')  
    
    tuned_dt = exp.tune_model(
        dt_model, 
        n_iter=n_iter, 
        optimize='F1', 
        search_library="optuna", 
        search_algorithm="tpe", 
        early_stopping=True
    )

    return tuned_dt

def compute_log_reg_metrics(model, x_test: pd.DataFrame, y_test):

    y_predict = model.predict_proba(x_test)

    log_loss_value = log_loss(y_test['shot_made_flag'].values, y_predict[:, 1])

    metrics = {'log_loss_lr': log_loss_value}

    return {
        key: {'value': value, 'step': 1}
        for key, value in metrics.items()
    }
    
def compute_decision_tree_metrics(model, x_test: pd.DataFrame, y_test):
  
    y_predict = model.predict(data=x_test)
    y_predict_scores = model.predict_proba(x_test)
 
    log_loss_value = log_loss(y_test['shot_made_flag'].values, y_predict_scores[:, 1])
    f1_score_value = f1_score(y_test['shot_made_flag'].values, y_predict)
    
    metrics = {
        'log_loss_dt': log_loss_value, 
        'f1_score_dt': f1_score_value
               }

    return {
        key: {'value': value, 'step': 1}
        for key, value in metrics.items()
    }