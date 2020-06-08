    Copyright(c) 2020-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+


# Python3: Data Structures & Algorithms
> Personal notes for DSA in Python3.


# Index

- [Trivial](#trivial)
- [Arrays](#arrays)


## Trivial

- Calculate Greatest Common Divisor (GCD, or HCF) of two numbers. <br>
    Functions 1-5 all solve the same problem, but differ in efficiency. Note the difference in computation-time of first & last implementations. <br>
    This builds a strong case for studying algorithms. <br>

    ```python
    #!/usr/bin/env python3

    def gcd1(m,n):
        '''
        No.of Steps ~ Number value
            eg. for 10^9 (=1 billion), about 1 billion steps are needed
        '''
        fm = [] # Factors of m
        fn = [] # Factors of n
        fc = [] # Common factors of m,n
        for i in range(1,m+1):
            if(m%i) == 0:
                fm.append(i)
        for j in range(1,m+1):
            if(n%j) == 0:
                fn.append(j)
        for f in fm:
            if f in fn:
                fc.append(f)
        return(fc[-1])

    def gcd2(m,n):
        fc = [] # Common factors of m,n
        for i in range(1,min(m,n)+1):
            if (m%i) == 0 and (n%i) == 0:
                fc.append(i)
        return(fc[-1])

    def gcd3a(m,n):
        for i in range(1,min(m,n)+1):
            if (m%i) == 0 and (n%i) == 0:
                mrcf = i    # Most-Recent-Common-Factor
        return(mrcf)

    def gcd3b(m,n):
        i = min(m,n)
        while (i>0):
            if (m%i) == 0 and (n%i) == 0:
                return(i)
            else:
                i -= 1

    def gcd4(m,n):
        # Assume m >= n
        if m<n:
            (m,n) = (n,m)
        while (m%n) != 0:
            d = m-n    # Utmost value is 1
            (m,n) = (max(n,d),min(n,d))
        return(n)

    def gcd5a(m,n):
        if m<n:
            (m,n) = (n,m)
        if m%n == 0:
            return(n)
        else:
            return(gcd7(n,m%n))

    def gcd5b(m,n):
        '''
        No.of Steps ~ No. of digits
            eg. for 10^9 (=10digits), about 10 steps are needed
        '''
        if m<n:
            (m,n) = (n,m)
        while (m%n) != 0:
            (m,n) = (n,m%n)
        return(n)
    ```


