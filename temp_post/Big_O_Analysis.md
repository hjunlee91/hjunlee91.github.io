---
layout: post
title: "What is the Big O Analysis?"
description: Learn what is the Big O Analysis
headline: What is the Big O Analysis?
modified: 2019-01-23
category: Data-Structure
tags: [Algorithm], [python]
imagefeature:
mathjax:
chart:
comments: true
---
What is the Big O Analysis?<br>
O in the Big O is **Omega**. In programming, time complexity is major issue to optimize the program.<br>
To compare the efficiency of algorithm, we usually use Big O analysis.<br>

There are two point in Big O notation.<br>
**First. Ignoring a constant term.**<br>
We assume that the input data is large enough and the efficiency of algorithm also affect by size of input data.<br>
So big O notation ignore a constant term.<br>
ex)<br>
```
O(2n) -> O(n)
```

**Second. Ignoring minor terms.**<br>
If input data is large, Bigest terms only impact on time complexity of algorithm.<br>
So big O notation ignore minor terms.<br>
ex)<br>
```
O(n^2 + 2n + 1) -> O)(n^2)
```
