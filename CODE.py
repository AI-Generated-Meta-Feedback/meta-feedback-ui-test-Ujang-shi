Algorithm SORT-BOOKS(books[1..n])
  for i ← 2 to n do
      key ← books[i]
      j ← i - 1
      while j ≥ 1 and (
            books[j].shelfNumber > key.shelfNumber OR
           (books[j].shelfNumber = key.shelfNumber AND
            books[j].returnOrder > key.returnOrder)
          ) do
          books[j + 1] ← books[j]
          j ← j - 1
      end while
      books[j + 1] ← key
  end for
  return books
End Algorithm
