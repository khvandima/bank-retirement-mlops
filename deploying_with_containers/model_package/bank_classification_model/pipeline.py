from sklearn.experimental import enable_iterative_imputer  # noqa: F401
from sklearn.impute import IterativeImputer
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier

from bank_classification_model.config.core import config


bank_pipe = Pipeline(
    steps=[
        (
            "imputer",
            IterativeImputer(random_state=config.model_config.random_state),
        ),
        (
            "xgb",
            XGBClassifier(
                objective="binary:logistic",
                eval_metric="auc",
                tree_method="hist",
                n_jobs=-1,
                random_state=config.model_config.random_state,
                colsample_bynode=0.8,
                colsample_bytree=0.6,
                gamma=0.1,
                grow_policy="depthwise",
                learning_rate=0.03,
                max_depth=4,
                max_leaves=15,
                min_child_weight=1,
                n_estimators=300,
                reg_alpha=0.01,
                reg_lambda=0.1,
                subsample=0.8,
            ),
        ),
    ]
)
