import pytest
from task_strings.valid_parentheses import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("maybe_valid, expected_result", [
    ("()", True),
    (")", False),
    ("([)", False),
    ("({[]})", True),
    ("}}}}}}(((())))", False),
    ("())", False),
    ("((((((((((((()))))))))))))", True),
])


def test_is_valid(solution, maybe_valid, expected_result):
    assert solution.is_valid(maybe_valid) == expected_result
