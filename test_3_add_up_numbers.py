# NOTE: You may NOT use the `sum()` function for exercise. Use a loop.

def add_up_numbers(arr):
  # Remove the `return None` code below and add your own code.
  answer3 = sum(arr)
  return answer3
# -----------------------------------------------------------------------------

# These are the automated tests for this exercise. Do not modify them at all.
# When you run `bin/check`, these tests will report on the validity of your
# algorithm.

def test_adds_two_numbers():
  assert add_up_numbers([3, 10]) == 13

def test_adds_three_numbers():
  assert add_up_numbers([20, 12, 51]) == 83

def test_handles_single_number():
  assert add_up_numbers([42]) == 42

def test_lots_of_numbers():
  assert add_up_numbers([23, 31, 89, 21, 2, 39, 202, 230, 142, 14]) == 793