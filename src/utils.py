# import os
# import sys
# import pickle
# from sklearn.metrics import r2_score
# from sklearn.model_selection import GridSearchCV

# from src.exception import CustomException

# def save_object(file_path: str, obj: object) -> None:
#     """
#     Saves a Python object (e.g., trained model, scaler, preprocessor) to disk using pickle.
#     """
#     try:
#         dir_path = os.path.dirname(file_path)
#         os.makedirs(dir_path, exist_ok=True)

#         with open(file_path, "wb") as file_obj:
#             pickle.dump(obj, file_obj)

#     except Exception as e:
#         raise CustomException(e, sys)


# def load_object(file_path: str) -> object:
#     """
#     Loads a saved Python object (e.g., preprocessor.pkl or model.pkl) from disk.
#     """
#     try:
#         with open(file_path, "rb") as file_obj:
#             return pickle.load(file_obj)

#     except Exception as e:
#         raise CustomException(e, sys)


# def evaluate_models(X_train, y_train, X_test, y_test, models: dict, param: dict) -> dict:
#     """
#     Trains and evaluates multiple Machine Learning models with hyperparameter tuning (GridSearchCV).
#     Returns a dictionary of model names and their corresponding test R2 scores.
#     """
#     try:
#         report = {}

#         for model_name, model in models.items():
#             model_params = param.get(model_name, {})

#             # Perform Grid Search CV for hyperparameter tuning
#             gs = GridSearchCV(model, model_params, cv=3)
#             gs.fit(X_train, y_train)

#             # Set best parameters to the model and train
#             model.set_params(**gs.best_params_)
#             model.fit(X_train, y_train)

#             # Predict on training and testing sets
#             y_test_pred = model.predict(X_test)

#             # Evaluate model performance on test set
#             test_model_score = r2_score(y_test, y_test_pred)

#             report[model_name] = test_model_score

#         return report

#     except Exception as e:
#         raise CustomException(e, sys)