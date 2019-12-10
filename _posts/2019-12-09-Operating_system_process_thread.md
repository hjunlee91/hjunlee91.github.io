---
layout: post
title: "What is the Operating System(OS)?"
description: Explain Operating system, process and thread
headline: Understand the Operating System
modified: 2019-12-09
category: Operating-System
tags: [OS]
imagefeature:
mathjax:
chart:
comments: true
---
This post is for the very beginner.<br>
What is the Operating System(OS)?<br>

Refer to Wikipedia, [An operating system](https://en.wikipedia.org/wiki/Operating_system)(OS) is system software that manages computer hardware, software resources, and provides common services for computer programs.<br>

![Imgur](https://i.imgur.com/tmSnJWB.png){: width="300" height="300"}

Let's think about Messenger program. **Program** is the executable instruction set to do some task.<br>
so the Messenger Program is file set of communication via message.<br>
If you use window, click any messenger program and ctrl + alt + delete.<br>
You can see the messenger program is running on the list of process.<br>

**Process** is <br>
1. Program that running on the OS continuously<br>
2. Task unit allocated *system resources* from OS<br>

Computer have to use finite hardware resources efficiently.<br>
Operating system distribute finite resources to process according to PCB(Process Control Block)<br>

Example of **System resources** are <br>
1. CPU time.<br>
2. Memory address to running program.<br>
3. Region of memory structure composed code, data, stack and heap.<br>

As beginner, Memory is quiet unfamiliar concept to understand.<br>
Let's think that computer also has limitation to understand and memorize something because of lack of memory like us.<br>

You might be confused several new concept.<br>
Let's think about **Ironman**. he need to fight with enemy, run a business and save person at the same time.<br>

![Imgur](https://i.imgur.com/yiTVVeY.jpg){: width="500" height="500"}

But he can do only one thing at once so he uses the **Ironman suit** to do all the task very quickly.<br>
So it looks everything is working at the same time for great effort of him<br>

Like this, One CPU Operating system shows hallucinations of many process running simultaneously<br>
to user with change the caring process quickly.<br>
How Operating system change the running process very quickly?<br>

![Imgur](https://i.imgur.com/GAWEMgh.png){: width="500" height="500"}

Before we click the Messenger program, it is located in **Hard drive** like SSD.<br>
It would be not proper comparing speed simply while Speed of SSD is 500 MB/s,<br>
CPU processor speed is 1GHz. It means Billions signal traverse the computer in one second.<br>

To overcome the speed difference, we are using **Computer memory** like RAM(Random Access memory).<br>
It is fast but stored information will be vanish when it turns off(we call it as *volatile memory*) <br>
and it is much expensive than hard drive. <br>

CPU also use **Cashe memory** to reduce the speed gap between CPU and Computer memory.<br>
Cashe memory is approximately 5 ~ 10 times faster than computer memory.<br>

![Imgur](https://i.imgur.com/u6HBrx8.png){: width="500" height="500"}

So back to process, process is running program on the processor(CPU). <br>
Process has at least one **thread**(main thread).<br>

Don't worry about it. this is the last new thing to learn in this post :) <br>
**Thread** is
1. Smallest sequence of executed instrument that can run using allocated resource from process.<br>
2. The unit that executing programmed instrument in the process.<br>

![Imgur](https://i.imgur.com/XFLONaG.png){: width="300" height="300"}

We will deep dive on the difference between process and thread later.<br>

*Summary*<br>
1. Computer has executable instruction file set as program.<br>
2. When program is running on the processor(CPU), it called as process.<br>
3. Operating system allocate system resources to process.<br>
4. thread is the unit that executing programmed instrument in the process.<br>
5. Process has at least one thread(main thread).<br>

Cheers.<br>
Thank You.<br>
