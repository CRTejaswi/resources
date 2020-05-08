    Copyright(c) 2019
    Author: Chaitanya Tejaswi(github.com / CRTejaswi)    License: MIT

# Notes: Python Programming Language (David Beazley) <sup>[\*](https://www.oreilly.com/library/view/python-programming-language/9780134217314/)</sup>
> Personal notes for the course.

- nextBus.py: Displays time - duration in which   the next bus(es) will arrive.

``` py
#! /usr/bin/env python3
import sys
import urllib.request
from xml.etree.ElementTree import XML


if len(sys.argv) != 3:
    raise SystemExit('Usage: nextBus.py route stopID')
route = sys.argv[1]
stopID = sys.argv[2]
url = urllib.request.urlopen(f'http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={stopID}&route={route}')
doc = XML(url.read())

for pt in doc.findall('.//pt'):
    print(pt.text)
```
```

```

- mortgage.py: Calculates mortgage interest rates.

``` py
#! /usr/bin/env python3

# Constants
principal = 500000
payment = 3500
rate = 0.05
emi_payment = 5000
emi_startMonth = 1
emi_stopMonth = 60
month = 0
paid = 0

while principal > 0:
    month += 1
    if month in range(emi_startMonth, emi_stopMonth + 1):
        total_payment = payment + emi_payment
    else:
        total_payment = payment
    interest = principal * (rate / 12)
    principal += (interest - total_payment)
    paid += total_payment
print(f'₹{paid} to be paid in {month//12} years, {month%12} months.')
```
```
₹576500 to be paid in 6 years, 7 months.
```

- X

``` py
```
```
```

- X

``` py
```
```
```

- X

``` py
```
```
```

- X

``` py
```
```
```

- X

``` py
```
```
```

- X

``` py
```
```
```

- X

``` py
```
```
```

- X

``` py
```
```
```
