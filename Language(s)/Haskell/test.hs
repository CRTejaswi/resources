import Data.List
import Data.Char
import System.IO

type Point2D = (Float, Float)

distance :: Point2D -> Point2D -> Float
distance (x1, y1) (x2, y2) = sqrt( sqr (x2-x1) + sqr (y2-y1) )
    where
        sqr :: Float -> Float
        sqr x = x * x

myPrimes n = sieve [2..n]
    where
        sieve (x:xs) = x:(sieve [y | y <- xs, mod y x > 0])

myLength :: [Int] -> Int
myLength l = foldr f 0 l
    where
        f _ x = x + 1

addMarks :: [[Int]] -> [Int]
addMarks = foldr1 (zipWith (+))

interleave :: a -> [a] -> [[a]]
interleave x [] = [[x]]
interleave x (y:ys) = (x:y:ys) : map (y:) (interleave x ys)

myPermutations :: [a] -> [[a]]
myPermutations [x] = [[x]]
myPermutations (x:xs) = concat (map (interleave x) (myPermutations xs))