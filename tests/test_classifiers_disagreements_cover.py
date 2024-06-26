
# Generated by CodiumAI
import pandas as pd
import pytest

from analysis_utils.classifiers_disagreements_cover import get_lb_disagreements, build_set_representation

class TestGetLbDisagreements:
    #  Tests that the function returns the expected output when provided with a valid input
    def test_happy_path_valid_input(self):
        # Arrange
        df = pd.DataFrame([[1, 1, 1]
                           , [2, 0, 0]
                           , [3, 0, 1]]
                        , columns=['K', 'A', 'B'])
        lb = ['A', 'B']
        key = 'K'
        actual = pd.DataFrame([[3, 'A', 'B']]
                        , columns=['K', 'first_function', 'second_function']
                                       )

        # Act
        result = get_lb_disagreements(df, lb, key)

        # Assert
        pd.testing.assert_frame_equal(result.reset_index(drop=True)
                                      , actual.reset_index(drop=True))


class TestBuildSetRepresentation:
    #  Tests that the function returns a list of sets containing unique values from valid keys when provided with a valid pandas DataFrame and a list of valid keys.
    def test_happy_path_valid_input(self):
        # Arrange
        df = pd.DataFrame([[3, 'A', 'B']]
                        , columns=['K', 'first_function', 'second_function']
                                       )

        key = 'K'

        # Act
        actual = build_set_representation(df, key)

        expected = [frozenset({3})]
        # Assert
        assert actual == expected
