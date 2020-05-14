def minmax(arr):
  """
  Takes a sequence of one or more numbers,
  and returns the smallest and largest numbers,
  in the form of a tuple of length two
  """
  min_n = arr[0]
  max_n = arr[0]
  if len(arr) == 1:
    return (arr[0], arr[0])
  elif len(arr) == 0:
    return None
  else:
    for x in range(len(arr)):
      if max_n < arr[x]:
        max_n = arr[x]
      if min_n > arr[x]:
        min_n = arr[x]
    return (min_n, max_n)
