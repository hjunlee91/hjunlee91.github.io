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
void DFS(Node root)
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
    while True:
        if len(stack) == 0:
            return None
        node = stack.pop()
        print(node.data)
        if node.data == Target:
            return node
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

BFS is Breadth-First search<br>
It start from the root, visit near nodes first and then go further node.<br>
We usually use this algorithm to find shortest route between two nodes.<br>

To avoid an infinite loof, we should check visited node.<br>
It use the FIFO(First-in First-out). repeated queue structure is used to here.<br>
It is similar to **prim**, **Dijkstra**


Pseudo code<br>

```
void BFS(Node node)
  Queue queue = new queue
  if root.visited == true
  queue.enqueue(root)

  while !queue.isEmpty()
    Node node = queue.dequeue()
    visit(node)

    for each Node n in node.adjacent
      if n.visited == False
        n.visited = True
        queue.enqueue
```

Python code<br>
queue<br>

```Python
Class Node:
  def __init__(node, data):
      node.data = data
      node.child = []

def bfs(node):
    queue = [node, ]
    while True:
        if len(queue) == 0:
            return None
        node = queue.pop(0)
        print(node.data)
        if node.data == Target:
            return node
        queue.extend(node.child)
```

It is quiet similar to DFS but we could not implement BFS as recursive structure.<br>
Those two search algorithm are quiet primitive method.<br>
But it is worth to use them when we solve some algorithm problem.<br>

According to [stackoverflow](https://stackoverflow.com/questions/3332947/when-is-it-practical-to-use-depth-first-search-dfs-vs-breadth-first-search-bf), we need to choose proper way to solve the problem.<br>

Simply, DFS might cause timeout on problem which have very rare solutions and deep tree.<br>
BFS might cause insufficient memory error on problem which have wide tree.<br>

My personal preference is like this<br>

1. bfs : find shortest path on simple graph<br>
2. dfs : find all possible solutions include complicated graph, tree and so on<br>

To implement properly we need to practice, write pseudo code first and implement the algorithm following the flow.<br>

Thank you<br>
