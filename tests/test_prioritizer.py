import pytest
from taskscore2.prioritizer import calculate_task_score


class TestPrioritizer:
    """
    Test class for the Prioritizer module.
    """

    def test_minimum_values(self):
        """
        Test case to verify the calculation of task score with minimum values.
        """
        assert calculate_task_score(1, 1) == 25

    def test_maximum_values(self):
        """
        Test case to verify the calculation of task score with maximum values.
        """
        assert calculate_task_score(4, 4) == 25

    def test_exception_values(self):
        """
        Test case to verify the handling of exception values in the calculation of task score.
        """
        with pytest.raises(ValueError):
            calculate_task_score(0, 3)
        with pytest.raises(ValueError):
            calculate_task_score(2, 5)
