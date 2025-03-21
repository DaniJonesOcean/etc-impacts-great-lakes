# src/pipeline.py

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import PowerTransformer, FunctionTransformer, MinMaxScaler, RobustScaler

def add_season(df):
    def assign_season(month):
        if month in [12, 1, 2]: return 'DJF'
        elif month in [3, 4, 5]: return 'MAM'
        elif month in [6, 7, 8]: return 'JJA'
        else: return 'SON'
    df['season'] = df['month'].apply(assign_season)
    return df

def clean_teleconnections(df):
    for col in ['tnh_value', 'tnh_bin', 'ep_np_value']:
        if col in df.columns:
            df.loc[df[col] < -9000, col] = np.nan
    return df

def build_transformer():
    return ColumnTransformer(
        transformers=[
            ('min_p_cent', PowerTransformer(method='box-cox'), ['min_p_cent']),
            ('max_p_grad', FunctionTransformer(np.log1p, validate=False), ['max_p_grad']),
            ('max_radius', FunctionTransformer(np.log1p, validate=False), ['max_radius']),
            ('max_uv', PowerTransformer(method='box-cox'), ['max_uv']),
            ('fraction_of_time_in_GLR', MinMaxScaler(), ['fraction_of_time_in_GLR']),
            ('maturity_glr0_minus_genesis_ratio', RobustScaler(), ['maturity_glr0_minus_genesis_ratio']),
        ],
        remainder='drop'
    )

def apply_transformer(transformer, df, feature_cols):
    transformed = transformer.transform(df[feature_cols])
    return pd.DataFrame(transformed, columns=feature_cols, index=df.index)
