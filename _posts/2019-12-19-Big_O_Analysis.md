---
layout: post
title: "What is the Big O Analysis?"
description: Learn what is the Big O Analysis
headline: What is the Big O Analysis?
modified: 2019-12-19
category: Data-Structure
tags: [Algorithm, python]
imagefeature:
mathjax:
chart:
comments: true
---
What is the Big O Analysis?<br>
O in the Big O is **Omega**. In programming, time complexity is major issue to optimize the program.<br>
To compare the efficiency of algorithm, we usually use Big O analysis.<br>

Big O notation usually means worst case except quick sort.<br>
in the case of quick sort, big o notation means average case.<br>
There are two point we should know.<br>

**First. Ignoring a constant term.**<br>
>We assume that the input data is large enough and the efficiency of algorithm also affect by size of input data.<br>
>So big O notation ignore a constant term.<br>
>ex)<br>
```
O(2n) -> O(n)
```

**Second. Ignoring minor terms.**<br>
>If input data is large, Bigest terms only impact on time complexity of algorithm.<br>
>So big O notation ignore minor terms.<br>
>ex)<br>
```
O(n^2 + 2n + 1) -> O(n^2)
```

![Imgur](https://i.imgur.com/rd2ILUs.jpg){: width="700" height="700"}

With mathematical prerequistes, we can compare the time complexity.<br>

**O(1) : constant**<br>
>Algorithm only take one step to solve the problem.<br>
>it takes same time without any impact from input data.<br>

**O(logN) : logarithmic**<br>
>Algorithm divide the problem as small quantity with same size and then solve it.<br>
>it's proportional to time but the data that we can solve is 2^N.<br>
>Binary search is a good example.<br>

**O(N) : linear**<br>
>Algorithm solve the problem linearly.<br>
>it's directly proprotional.<br>
>For, linear search are a good example.<br>

**O(NlogN) : super linear**<br>
>Algorithm divide the problem as small quantity and then merge the result after solve each of them.<br>
>it's proportional but it would take much more than linear.<br>
>Quick sort and Merge sort are a good example.<br>

**O(N^2) : quadratic**<br>
>Algorithm solve the problem using double for statement.<br>
>if input is large enough, time is increasing exponentailly.<br>
>This is not a good way to solve the problem.<br>
>double for statement, insertion sort, bubble sort are a good example.<br>

So let's practice to calculate the big O notation.

```python
def func(a+b) :
  return a+b # O(1)

print(func(10+20))
```

Nonetheless the size of input data, this func works only one time.<br>
It is definitely O(1). <br>


```python
def func(value) :
  print(value) # O(1)
  for i in range(value) :
    print(i, end=', ') # O(N)

func(10)
```

print value is happening only one time when the func is called. -> O(1).<br>
For state has range as value. so time complexity increase proportional -> O(N).<br>
Big O notation ignore the minor factor.<br>
```
O(N) + O(1) -> O(N)
```

Let's think about binarySearch. To find a target number in the array, binarySearch divide<br>
the problem to small quantity<br>

```python
def binarySearch (arr, left, right, target):
    if r >= l;
        if r >= l:
            mid = l + (r - l)/2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return binarySearch(arr, left, mid-1, target)
            else:
                return binarySearch(arr, mid+1, right, target)
    else:  
        return -1

arr = [ 50, 10, 30, 20, 40, 60, 70, 90 ]
target = 10
result = binarySearch(arr, 0, len(arr)-1, target)

if result != -1:
    print "Element is present at index %d" % result
else:
    print "Element is not present in array"
```

![Imgur](https://i.imgur.com/iA8DlQa.png){: width="700" height="700"}

So that's why binarySearch has O(logN).<br>
the point is divide the problem as smaller one.<br>

like this we can compare the time complexity using Big O analysis.<br>
Practice to calculate Big O to simple code.<br>

furthur more, **space complexity** is the measure that how algorithm use memory efficiently.<br>
Developer should develop algorithm considering both complexity.<br>

Thank you.
