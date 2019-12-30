---
layout: post
title: "What is the DFS and BFS?"
description: Learn what is the DFS and BFS
headline: What is the DFS and BFS?
modified: 2019-01-23
category: Data-Structure
tags: [Algorithm], [python]
imagefeature:
mathjax:
chart:
comments: true
---

When we try to search the shortest route, There are a lot of way to search.<br>
Today, we take a look two represented search algorithm, DFS and BFS.<br>

First DFS is Depth-First Search.<br>
It start from the root, search whole branch before move to the next branch.<br>

Simply DFS same as the way to find the route in the maze with one's hand on the wall.<br>
If the traveller arrive the dead end, turn around and find other way on the latest fork.<br>
We usually use this way to search every node.<br>

DFS is recursive format so it should check the visited node to avoid an infinite loof.<br>

We can implement DFS using stack or recursive function.<br>

Pseudo code<br>

```
def DFS(Node root)
  if root == null: // if the root is null, return
    return
  else:
    visit(root)
    root.visited = true // check the root as visited
    for each Node n in root.adjacent:
      if n.visited == false: // keep search on the unvisited root
        DFS(n)
```

Python code<br>
stack<br>

```Python
Class Node:
  def __init__(node, data):
      node.data = data
      node.child = []

def dfs(node):
    stack = [node, ]
    visited = set()
    while True:
        if len(stack) == 0:
            return None
        node = stack.pop()
        print(node.data)
        if node.data == Target:
            return node
        if node in visited:
            continue
        stack.extend(node.child)
```

recursive<br>

```Python
Class Node:
  def __init__(node, data):
      node.data = data
      node.child = []
      node.visited = False

def dfs(node):
    if node.visited == True:
        return
    print(node.data)
    node.visited = True
    if node.data == Target:
        return node
    for child in node.child:
        dfs(child)
```