    Copyright(c) 2019
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+


# Haskell
> Notes for Haskell language.

- Courses
    - [x] [Haskell (NPTEL)](https://nptel.ac.in/courses/106/106/106106137/)
    - [ ] [Haskell (Stanford)](http://www.scs.stanford.edu/14sp-cs240h/slides/)
    - [ ] [Haskell (UPenn)](https://www.cis.upenn.edu/~cis194/spring13/lectures.html)
    - [ ] [Haskell (edX)](https://www.edx.org/course/introduction-to-functional-programming)

- Docs
    - [Haskell](https://downloads.haskell.org/~ghc/latest/docs/html/libraries/)
    - [GHC API](https://downloads.haskell.org/~ghc/latest/docs/html/libraries/ghc-8.8.1/index.html)
    - [Tutorial](https://wiki.haskell.org/Meta-tutorial)
    - [Recipies](https://wiki.haskell.org/Cookbook)
    - [Lists](https://wiki.haskell.org/How_to_work_on_lists)

- [Books](https://wiki.haskell.org/Books)
    - [Programming in Haskell (Hutton)](file:///B:/CRTejaswi/Documents/Books/Tech/05%20-%20Computer%20Science%20Engineering/03%20-%20Languages/Haskell/Haskell%20(Hutton).pdf)
    - [Real World Haskell (O'Sullivan)](https://github.com/tssm/up-to-date-real-world-haskell)
    - [Haskell In Depth (Bragilevsky)](https://www.manning.com/books/haskell-in-depth)

## Functional Programming (Haskell, Python)

- http://www.cs.nott.ac.uk/~pszgmh/afp.html
- https://www.youtube.com/watch?v=mlTO510zO78
- https://github.com/facebook/Haxl


### Don't Care

`_` is used to represent don't care variables.
It doesn't reference a variable, hence it cannot be used anywhere out of the expression.

``` hs
and :: Bool -> Bool -> Bool
and True b = b
and False b = False

and :: Bool -> Bool -> Bool
and True b = b
and False _ = False

or :: Bool -> Bool -> Bool
or True b = True
or b True = True
or b1 b2  = False

or :: Bool -> Bool -> Bool
or True _ = True
or _ True = True
or _ _    = False

nand :: Bool -> Bool -> Bool
nand False _ = True
nand _ False = True
otherwise    = False
```

### Conditional Definitions


### Examples
- Greatest Common Divisor (GCD)
> Determine the GCD (or HCF) of two numbers.

    This example makes use of Euclid's division lemma.
    ``` hs
    gcd :: Int -> Int -> Int
    gcd m 0 = m
    gcd m n
        | m >= n    = gcd n (mod m n)
        | otherwise = gcd n m
    ```

- Largest Divisor
> Determine the largest number `k; k<n` that divides `n` .

    This example makes use of an auxiliary function (main function depends on another function for its result).

    ``` hs

    ```

- Integer Logarithm
> Find the integer-logarithm of a number `n`.

    `intlogn y = k` is the integer-only value of `logn y` ; i.e. `n^k = y; k is an integer`.

    - Dividing y by n, k times gives a value >= 1.
    - Dividing y by n, k+1 times gives a value < 1.

    ``` hs

    ```

- Reversing The Digits
> Problem Statement.

    Notes here.

    ``` hs

    ```

- Topic
> Problem Statement.

    Notes here.

    ``` hs

    ```

## Lists

Lists are sequences of values of a uniform type. Unlike Python, which allows inclusion of multiple types in the same list, Haskell strictly takes only values of the same type.

(See Vid#9)
reverse, head/tail, init/last, take/drop, length, sum.

- List with values of type `T` has type `[T]` <br>
    eg. [1,2,3,4] :: [Int], [True, False, True] :: [Bool]
- Lists can be nested. <br>
    eg. [[2,3], [], [0,1,0]] :: [[Int]]
- Appending to List <br>
    eg. 1: [2,3] => [1,2,3], 1:2:[3] => [1,2,3]
- Decomposing List (head/tail) <br>
    eg.
- Defining functions on lists <br>

- Range of Values
Arithmetic progressions, Counting backwards,

    ``` hs
    [1..10]    => [1,2,3,4,5,6,7,8,9,10]

    [1,3,..10] => [1,3,5,7,9]
    [2,5..20]  => [2,5,8,11,14,17,20]

    [8..5]     => []
    [8,7..5]   => [8,7,6,5]
    ```

### Examples

- Length of a list

    ``` hs
    myLength :: [Int] -> Int
    myLength [] = 0
    myLength l = 1 + myLength (tail l)

    myLength :: [Int] -> Int
    myLength [] = 0
    myLength (x:xs) = 1 + myLength xs

    >> myLength [1..10]
    10
    ```

- Sum of values in a list

    ``` hs
    mySum :: [Int] -> Int
    mySum [] = 0
    mySum (x:xs) = x + mySum xs

    >> mySum [1..10]
    55
    ```

- Appending values to the right

    Append values to the end of `tail`.
    ```
    appendRight :: Int -> [Int] -> [Int]
    appendRight n = [n]
    appendRight n (x:xs) = x : (appendRight n xs)
    ```

- Merge two lists

    ``` hs
    myMerge :: [Int] -> [Int] -> [Int]
    myMerge [] l = l
    myMerge (x:xs) l = x : (myMerge xs l)

    >> myMerge [1..5] [5,4..1]
    [1,2,3,4,5,5,4,3,2,1]
    >> [1..5] ++ [5,4..1]
    [1,2,3,4,5,5,4,3,2,1]
    ```

- Reverse a list

    ``` hs
    myReverse :: [Int] -> [Int]
    myReverse [] = []
    myReverse (x:xs) = (myReverse xs) ++ [x]
    ```

- Check if list is sorted

    ``` hs
    isSortedUp :: [Int] -> Bool
    isSortedUp [] = True
    isSortedUp [x] = True
    isSortedUp (x:y:ys) = (x <= y) && isSortedUp (y:ys)

    isSortedDown :: [Int] -> Bool
    isSortedDown [] = True
    isSortedDown [x] = True
    isSortedDown (x:y:ys) = (x >= y) && isSortedDown (y:ys)
    ```

- Check if a list of integers is (strictly) alternating

``` hs

```

- Filter In/Out first n elements of a list

    ``` hs
    myTake :: Int -> [Int] -> [Int]
    myTake _ [] = []
    myTake n (x:xs)
        | n <= 0 = []
        | n > 0  = x : (myTake (n-1) xs)

    myDrop :: Int -> [Int] -> [Int]
    myDrop _ [] = []
    myDrop n xs@(y:ys)
        | n <= 0 = xs
        | n > 0  = myDrop (n-1) ys

    >> myTake 3 [1..5]
    [1,2,3]
    >> myDrop 3 [8..15]
    [11,12,13,14,15]
    ```

## Characters/Strings

A character is of type __Char__.
A string is a sequence of __Char__, and has the type __String__ or __[Char]__.
```
['h','e','l','l','o'] == "hello"
"" = []
```

### Examples

- Capitalize a character

    ``` hs
    capitalize :: Char -> Char
    capitalize ch
        | (ch >= 'a' && ch <= 'z') = chr (ord ch + (ord 'A' - ord 'a'))
        | otherwise = ch
    ```

- Search for character in a string

    ``` hs
    myisChar :: Char -> String -> Bool
    myisChar _ "" = False
    myisChar c (x:xs)
        | c == x    = True
        | otherwise = myisChar c xs
    ```

- Convert a string to uppercase

    ``` hs
    mytoUpper :: String -> String
    mytoUpper "" = ""
    mytoUpper (x:xs) = (capitalize x) : (toUpper xs)

    capitalize :: Char -> Char
    capitalize ch
        | (ch >= 'a' && ch <= 'z') = chr (ord ch + (ord 'A' - ord 'a'))
        | otherwise = ch
    ```

- Get first position of character in string

    ``` hs
    myPosition :: Char -> String -> Int
    myPosition c "" = 0
    myPosition c (x:xs)
        | c == x = 0
        | otherwise = 1 + (myPosition c xs)
    >> myPosition 'w' "Hello World"
    11
    >> myPosition 'W' "Hello World"
    6
    ```

- Count the number of words in a string

    ``` hs
    -- Define whitespace
    whitespace :: Char -> Bool
    whitespace ' '  = True
    whitespace '\t' = True
    whitespace '\n' = True
    otherwise _     = False

    -- Define wordCounter
    wordCounter :: String -> Int
    wordCounter [c] = 0
    wordCounter (c:x:xs)
        | (whitespace c) && not (whitespace x) = 1 + wordCounter (x:xs)
        | otherwise = wordCounter (x:xs)

    -- Append ' ' at beginning of string.
    wordCount :: String -> Int
    wordCount s = wordCounter (' ':s)

    >> wordCount "My name is Slim Shady."
    5
    ```

## Tuples

Tuples are sequences of values of a different types.

- Type
```
("John Doe", 12, "18-12-1999") :: (String, Int, String)
[("John", 92), ("Jamie", 86), ("Jeany", 96)] :: [(String, Int)]
```
### Examples

- Sum of pairs of integers

    ``` hs
    sumPair :: (Int, Int) -> Int
    sumPair (x,y) = x + y

    sumPairs :: [(Int, Int)] -> Int
    sumPairs [] = 0
    sumPairs ((x,y):zs) = x + y + sumPairs zs

    >> sumPair (2,3) + sumPairs [(1,1),(2,2),(3,3)]
    17
    ```

- Lookup marks by name

    ``` hs
    marksLookup :: String -> [(String, Int)] -> Int
    marksLookup s [] = -1
    marksLookup s ((name, marks):xs)
        | (s == name) = marks
        | otherwise   = marksLookup s xs

    >> marksList = [("John", 92), ("Jamie", 86), ("Jeanie", 96)]
    >> marksLookup "Jeanie" marksList
    96
    ```

- 2D Points

    ``` hs
    type Point2D = (Float, Float)

    distance :: Point2D -> Point2D -> Float
    distance (x1, y1) (x2, y2) = sqrt( sqr (x2-x1) + sqr (y2-y1) )
        where
            sqr :: Float -> Float
            sqr x = x * x
    >> distance (0,0) (2,3)
    3.6055512
    ```

### List Comprehensions

- Prime Numbers: Sieve of Eratosthenes
    ``` hs
    myPrimes n = sieve [2..n]
    where
        sieve (x:xs) = x:(sieve [y | y <- xs, mod y x > 0])
    >> myPrimes 100
    [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
    *** Exception: test.hs:15:9-59: Non-exhaustive patterns in function sieve
    ```
- Length Of A List
    ``` hs
    myLength :: [Int] -> Int
    myLength [] = 0
    myLength (x:xs) = 1 + myLength xs
    >> myLength [1,2,3]
    3

    myLength :: [Int] -> Int
    myLength l = foldr f 0 l
    where
        f _ x = x + 1
    >> myLength [1,2,3]
    3
    ```

### List: Functions

- `take`/`drop`: take/drop first `n` elements.
- `takeWhile`/`dropWhile`: take/drop until criteria matches.

    ``` hs
    myPermutations :: [a] -> [[a]]
    myPermutations [x] = [[x]]
    -- myPermutations (x:xs) = concat (map (interleave x) (myPermutations xs))
    myPermutations (x:xs) = concatMap (interleave x) (myPermutations xs)

    >> myPermutations [1,2,3]
    [[1,2,3],[2,1,3],[2,3,1],[1,3,2],[3,1,2],[3,2,1]]
    >> myPermutations ["my name","is","Chaitanya"]
    [["my name","is","Chaitanya"],["is","my name","Chaitanya"],["is","Chaitanya","my name"],["my name","Chaitanya","is"],["Chaitanya","my name","is"],["Chaitanya","is","my name"]]
    ```