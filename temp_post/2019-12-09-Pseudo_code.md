---
layout: post
title: "How to write a Pseudo-Code"
description: Explain How to write a Pseudo-code
headline: Understand the pseudo-code
modified: 2019-12-09
category: Programming
tags: [Programming], [Algorithm], [C]
imagefeature:
mathjax:
chart:
comments: true
---
How to write a Pseudo-code?<br>

Sometimes we need to explain how it works to other engineer, custormer or project manager. <br>
But most of them is not expert to our area. How do we do explain the logic to them?<br>

There is three way to explain the logic<br>

1. Natural language<br>
2. Flow chart<br>
3. Pseudo-code<br>

**Pseudo** is a prefix that represent "not genuine" "imitating".<br>
**Pseudo-code** is not actual code but easy to write without programming background and knowledge.<br>
Actually there is no standard syntax for writing the psuedo-code, Pseudo-code is not an executable program,<br>
it is methodology to explain the logic to others. Flow charts is graphical method of Pseudo-code.<br>

Even though it is not a actual code. We need to think about a few rule to communicate with others.<br>
For example, if we are trying to get sum of numbers from 1 to 100.<br>

it is simple so we can make it as actual code easily like this.<br>

```c
  int sum = 0;
  int number = 1;
  do {
    sum = sum + number;
    number++;
  } while(number != 101);

  printf("the result is [%d]", sum);
```
We can express this logic as pseudo-code like this.<br>

```
BEGIN
SET SUM TO 0
SET NUMBER TO 1

WHILE NUMBER < 101
COMPUTE SUM AS SUM + NUMBER
INCREMENT NUMBER
ENDWHILE

PRINT SUM
END
```

If we need to add some logic inside of repeat, we can use the **tap** to make it clear.<br>

```
BEGIN
SET SUM TO 0
SET NUMBER TO 1

WHILE NUMBER < 101
COMPUTE SUM AS SUM + NUMBER
  IF SUM > 3000 THEN
  PRINT TEXT TO "I love you over 3000"
  ENDIF
INCREMENT NUMBER
ENDWHILE

PRINT SUM
END
```

For practice, let's think about ATM. <br>

we offer three services to customer. <br>

1. checkBalance<br>
2. withdrawal<br>
3. deposit<br>

Before we offer services we need to heck ATM machine status and PIN number to validate the card.<br>

1. checkAvailable<br>
2. checkPIN<br>
3. services<br>

```
ATM MAIN
BEGIN
  WHILE

  ENDWHILE
END
