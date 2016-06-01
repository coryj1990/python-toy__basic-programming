def is_greater_than_five(num):
  # Remove the `return None` code below and add your own code.
  if num > 5:
      return True
  else:
      return False

# -----------------------------------------------------------------------------

# These are the automated tests for this exercise. Do not modify them at all.
# When you run `bin/check`, these tests will report on the validity of your
# algorithm.

def test_ten_is_greater_than_five():
  assert is_greater_than_five(10)

def test_30_is_greater_than_five():
  assert is_greater_than_five(30)

def test_1_is_smaller_than_five():
  assert is_greater_than_five(1) == False

def test_5_is_not_greater_than_five():
  assert is_greater_than_five(5) == False