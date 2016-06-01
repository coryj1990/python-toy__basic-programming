def uppercases_all_letters(str):
  # Remove the `return None` code below and add your own code.
  answer2 = str.upper()
  return answer2

# -----------------------------------------------------------------------------

# These are the automated tests for this exercise. Do not modify them at all.
# When you run `bin/check`, these tests will report on the validity of your
# algorithm.

def test_hello():
  assert uppercases_all_letters("hello") == "HELLO"

def test_HELLO():
  assert uppercases_all_letters("HELLO") == "HELLO"

def test_scooby_doo():
  assert uppercases_all_letters("scooby doo") == "SCOOBY DOO"