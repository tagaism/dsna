def is_even(k):
  """
  Takes an integer value and
  returns True if k is even,
  and False otherwise.
  """
  if k < 0:
    k *= -1
  while k > 0:
    k -= 2
  return k == 0