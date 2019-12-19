---
layout: post
title: "What is the Binary search?"
description: Learn what is the Binary search
headline: What is the Binary search?
modified: 2019-12-20
category: Data-Structure
tags: [Algorithm, python]
imagefeature:
mathjax:
chart:
comments: true
---
**BinarySearch algorithm** is search algorithm in the sorted data set.<br>
it can not apply to unsorted data set.<br>

Let's take a look step by step. assume the data set is already ascending sorted.<br>

First, Check the middle of data set.<br>

![Imgur](https://i.imgur.com/XbH7XDx.png){: width="700" height="700"}

Compare middle to target number.<br>.

if the middle is larger than target, we don't need to take care about right side of middle.<br>

![Imgur](https://i.imgur.com/uh6rYxM.png){: width="700" height="700"}

find the middle in the left part.<br>

![Imgur](https://i.imgur.com/NcAFOft.png){: width="700" height="700"}

repeat until find the target number.<br>

![Imgur](https://i.imgur.com/dGlV0kO.png){: width="700" height="700"}

we can implement this by two way. using recursive function or while statement.<br>

**resursive function**<br>
```python
def binarySearch(arr, left, right, target):
    if right >= left: # if the data set is descending
        if right >= left:
            mid = left + (right - left)/2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return binarySearch(arr, left, mid-1, target)
            else:
                return binarySearch(arr, mid+1, right, target)
    else:
        return -1

arr = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
target = 1
result = binarySearch(arr, 0, len(arr)-1, target)

if result != -1:
    print "Element is present at index %d" % result
else:
    print "Element is not present in array"
```

**while statement**<br>
```python
def binarySearch(arr, left, right, target):
    if right >= left:
        while right >= left:
            mid = left + (right - left)/2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    else:
        return -1

arr = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
target = 1
result = binarySearch(arr, 0, len(arr)-1, target)

if result != -1:
    print "Element is present at index %d" % result
else:
    print "Element is not present in array"
```

you can see the result using the [IDEONE](https://ideone.com/ideone/Index/submit/)<br>

next time, we will take a binary search tree.<br>

Thank you.
