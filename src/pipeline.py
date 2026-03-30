# src/pipeline.py

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import PowerTransformer, FunctionTransformer, MinMaxScaler, RobustScaler

def add_season(df):
    def assign_season(month):
        if month in [1, 2, 3]: return 'JFM'
        elif month in [4, 5, 6]: return 'AMJ'
        elif month in [7, 8, 9]: return 'JAS'
        elif month in [10, 11, 12]: return 'OND'
        else: return 'ERR'
    df['season'] = df['month'].apply(assign_season)
    return df

def clean_teleconnections(df):
    for col in ['tnh_value', 'tnh_bin', 'ep_np_value']:
        if col in df.columns:
            df.loc[df[col] < -9000, col] = np.nan
    return df

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer


def build_transformer():
    """
    Build a minimal, physically interpretable preprocessing transformer
    for unsupervised clustering.

    Strategy:
    - Apply log1p to strictly positive, right-skewed variables
    - Leave bounded or dimensionless variables in native scale
    - Avoid distribution-shaping transforms that obscure physical meaning
    """

    log1p_vars = [
        "max_p_grad",
        "max_radius",
        "max_uv",
    ]

    passthrough_vars = [
        "min_p_cent",
        "fraction_of_time_in_GLR",
        "maturity_glr0_minus_genesis_ratio",
    ]

    return ColumnTransformer(
        transformers=[
            (
                "log1p",
                FunctionTransformer(np.log1p, validate=False),
                log1p_vars,
            ),
            (
                "pass",
                "passthrough",
                passthrough_vars,
            ),
        ],
        remainder="drop",
        verbose_feature_names_out=False,
    )


def build_impact_transformer():
    return ColumnTransformer(
        transformers=[
            ("precip", FunctionTransformer(np.log1p, validate=False), [
                'sup_ttl_precip', 'mi_ttl_precip', 'huron_ttl_precip',
                'erie_ttl_precip', 'ont_ttl_precip'
            ]),
            ("evap_anom", PowerTransformer(), [
                'sup_ttl_evap_anom', 'mi_ttl_evap_anom', 'huron_ttl_evap_anom',
                'erie_ttl_evap_anom', 'ont_ttl_evap_anom'
            ])
        ],
        remainder="drop"
    )

def apply_transformer(transformer, df, feature_cols):
    transformed = transformer.transform(df[feature_cols])
    return pd.DataFrame(transformed, columns=feature_cols, index=df.index)
