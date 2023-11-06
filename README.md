# wikihow_most_helpful_article_predictor
This [dataset](https://www.kaggle.com/datasets/aniketsharma00411/wikihow-features) contains a collection of more than 19,000 how-to guides publicly available on wikiHow. The data is extracted using the open-source API wikihowunofficialapi. The extracted text has been scored by the wikiHow users on a scale of 0 to 100, representing their helpfulness. The model will be used to predict which article will score high or low based on our features.
I have created a [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) for each of these models, such that the data transformations and model training/prediction steps are assembled together.

The prediction is a regression problem, so I have trained three models:
[LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html), [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) and [XGBRegressor](https://xgboost.readthedocs.io/en/latest/python/python_api.html#xgboost.XGBRegressor).
I have done EDA.
