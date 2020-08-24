import pandas as pd
from pandas.testing import assert_frame_equal
import pytest

from monotonocity_utils import evaluate_monotonocity

@pytest.mark.parametrize(('df'
                            , 'relevant_columns'
                            , 'monotone_column'
                            , 'monotone_order'
                            , 'expected')
    , [
pytest.param(
            pd.DataFrame([
                ['reduced_risk', 0, 1],
                ['other', 0, 1],
                ['other', 1, 1],
                ['hotspot', 1, 0],
            ], columns=['quality_group', 'f1', 'f2'])
            , ['f1', 'f2']
            , 'quality_group'
            , ['reduced_risk', 'other', 'hotspot']
            , pd.DataFrame([
                ['f1', True],
                ['f2', False],
    ], columns=['feature', 'monotonicity'])

, id='reg1')
                         ])
def test_evaluate_monotonocity(df : pd.DataFrame
                           , relevant_columns
                           , monotone_column
                           , monotone_order
                      , expected):

    actual = evaluate_monotonocity(df
                           , relevant_columns
                           , monotone_column
                           , monotone_order)

    assert_frame_equal(actual, expected)

