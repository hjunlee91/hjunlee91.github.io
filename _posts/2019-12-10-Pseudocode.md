---
layout: post
title: "How to write a Pseudocode"
description: Explain How to write a Pseudocode
headline: Understand the pseudocode
modified: 2019-12-10
category: Programming
tags: [Programming, Algorithm]
imagefeature:
mathjax:
chart:
comments: true
---

How to write a Pseudocode?<br>

Sometimes we need to explain how it works to other engineer, custormer or project manager. <br>
But most of them is not expert to our area. How do we do explain the logic to them?<br>

There is three way to explain the logic<br>

1. Natural language<br>
2. Flow chart<br>
3. Pseudo-code<br>

**Pseudo** is a prefix that represent "not genuine" "imitating".<br>
**Pseudo-code** is not actual code but easy to write without programming background and knowledge.<br>
Actually there is no standard syntax for writing the psuedocode, Pseudo-code is not an executable program,<br>
it is methodology to explain the logic to others. Flow charts is graphical method of Pseudocode.<br>

Even though it is not a actual code. We need to think about a few rule to communicate with others.<br>
For example, if we are trying to get sum of numbers from 1 to 100.<br>

It is simple so we can make it as actual code easily like this.<br>

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
PROCEDURE SUM_NUMBER

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
PROCEDURE SUM_NUMBER

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

Before we offer services we need to heck ATM machine status, card inserted and PIN number to validate the card.<br>

1. checkATMWorks<br>
2. checkInsertCard<br>
3. checkPIN<br>
4. services<br>

```
PROCEDURE ATM_MAIN
BEGIN
  WHILE
    IF checkATMWorks is disabled
      PRINT TEXT TO "ATM IS NOT AVAILABLE"
    ELSE
      IF checkInsertCard is true
        call checkPIN
      ELSE
        PRINT TEXT TO "INSERT CARD"
      ENDIF
    ENDIF
  ENDWHILE
END
```

Machine must be working and Card should be inserted to validate PIN.<br>

```
PROCEDURE checkPIN
BEGIN
  SET MAXPIN TO 3
  SET PINCOUNT TO 0
  STORE THE CardData FROM ReadCard
  WHILE UNTIL PINCOUNT EQUAL TO MAXPIN
    INPUT PIN FROM KEYPAD
    INCREMENT PINCOUNT
  ENDWHILE
  IF PIN EQUAL TO CardData.PIN
    call services
  THEN
    PRINT TEXT TO "WRONG PIN"
    EXIT checkPIN
  ENDIF
END
```

Before offer the services, we need to check the PIN.<br>

```
PROCEDURE services
VALUEABLE
  SET BALANCE AS CardData.BALANCE
BEGIN
  INPUT SELECTION FROM KEYPAD
  CASE OF SELECTION
    WHEN checkBalance
      PRINT BALANCE
    WHEN withdrawal
      INPUT WITHDRAWAL_MONEY FROM KEYPAD
      IF WITHDRAWAL_MONEY > BALANCE
        PRINT TEXT TO "Not enough balance"
      ELSE
        WITHDROWAL MONEY
      ENDIF
    WHEN deposit
      INPUT DEPOSIT_MONEY FROM KEYPAD
      GET INSERTTED_MONEY FROM MACHINE
      IF INSERTED_MONEY EQUAL TO DEPOSIT_MONEY
        SET BALANCE AS BALANCE + DEPOSIT_MONEY
      ELSE
        RETURN INSERTED_MONEY FROM MACHINE
      ENDIF
    DEFAULT
      RETURN THE CARD TO CUSTOMER
  ENDCASE
END
```

we can check the balance from card data, using this to show the balance and withdrawal.<br>

This is just a example to show how to write a pseudocode.<br>
It depends on that who is the audience, what is the pupose etc..<br>
Write any simple logic as pseudo-code. it would be helpful to understand it<br>

Cheers<br>
Thank you<br>
