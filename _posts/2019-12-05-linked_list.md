---
layout: post
title: "What's <br>a Linked List"
description: Explain a linked list.
headline: Let's find out about a Linked list.
modified: 2019-12-05
category: Data-Structure
tags: [C]
imagefeature:
mathjax:
chart:
comments: true
---

This post is for the very beginner.<br>
Linked list is quiet good example to explain struct, pointer and memory.<br>
Let's think about when we stand in line.<br>

![Imgur](https://i.imgur.com/sCP6WZD.jpg)

We usually don't know what order i'm standing in at the front. However we know who stand just in front us.<br>
Like this, let's guess we are a "NODE", we have two information.<br>
First one is the person who stand in front us.<br>
Second one is a data like height. so we can write code like this<br>

```c
typedef struct NODE {
  struct NODE* next; // Point out next struct *memory address* **using pointer( * )**
  int data; // Store a data like height
}node; // define this kind of NODE struct as "node"
```

<br>
**struct NODE* next**<br>
All the data has a memory address to stored.<br>
*struct NODE next* replaced NODE* cause error because it is trying that define the same struct in the struct.<br>
To have information for next person, We should point out memory address of next NODE.<br>

![Imgur](https://i.imgur.com/QT6yFfn.jpg)

a woman wearing backpack also has information for next and data.<br>
From the void, we need to reference point.<br>

```c
node* head = (node*)malloc(sizeof(node*)); // dynamically allocate memory size as much as node* structure. it returns memory address.
node* tail = (node*)malloc(sizeof(node*));

head->next = tail; // tail is head->next
tail->next = NULL; // NULL is tail->next
```

**pointer** is used to point out *memory address* so we need to dynamically allocate memory.<br>
A = B is meaning that put B data to A. B is A.<br>

```c
void addNode(node* head, int data) {
	node* new_node = (node*)malloc(sizeof(node*)); // Make a new node to add
	new_node->next = head->next; // new node next point out the point that head pointed.
	head->next = new_node; // head point out the new node
	new_node->data = data;
}
```

Let's think that someone cut in line.<br>
someone is coming.<br>
this guy stand behind the woman wearing the backpack.<br>
Now I am standing behind the bad guy.<br>

```c
void deleteNode(node* head) {
	node* target_node = head->next; // point out node next to head
	head->next = target_node->next;
	free(target_node); // free the momory
}
```

Let's point out someone in front of me.<br>
the guy in front of other guy will be the one that in front of me.<br>
he will leave from the line.<br>

```c
void bubbleSort(node* head) {
	node* target_node = head->next;
	bool sort_happen = false;
	int temp = -1;
	do {
		sort_happen = false;
		while(target_node->next->next != NULL) {
			if(target_node->data > target_node->next->data) {
				printf("%d target_node->data, %d target_node->next->data changed", target_node->data, target_node->next->data);
				temp = target_node->data;
				target_node->data = target_node->next->data;
				target_node->next->data = temp;
				sort_happen = true;
				printf("\n");
			}
			target_node = target_node->next;
		}
		target_node = head->next;
	} while(sort_happen != false);
}
```

Bubblesort is one of the sorting. We will take a look later.<br>
Let's think that stand in the line follow the height order.<br>
Bubblesort is comparison that 1:1 comparing to data, if I'm taller than next person, change the position.<br>
After one cycle, the tallest one is stand the first of the line.<br>
We repeat sorting until there is no change the position.<br>

```c
void printNode(node* head) {
	node* target_node = head->next; // point out the node next to head
	while(target_node->next != NULL) {
		printf("%d ", target_node->data);
		target_node = target_node->next; // move to the next node
	}
	printf("\n");
}
```

print the data is traverse the node until tail.<br>

Point of linked list is memory and address.<br>
**" * "** pointer is used to point out address.<br>
If you understand the concept. it would be easy to understand.<br>

Please refer to the full code and test on [IDEONE](https://ideone.com/ideone/Index/submit/) <br>
If you have a question, please leave a comment on the post.<br>

Thank you.<br>

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct NODE {
  struct NODE* next;
  int data;
}node;

void addNode(node* head, int data);
void deleteNode(node* head);
void bubbleSort(node* head);
void printNode(node* head);

int main() {

	node* head = (node*)malloc(sizeof(node*));
	node* tail = (node*)malloc(sizeof(node*));

	head->next = tail;
	tail->next = NULL;

	addNode(head, 10);
	addNode(head, 30);
	addNode(head, 70);
	addNode(head, 90);
	addNode(head, 20);
	addNode(head, 15);

	printNode(head);

	deleteNode(head);

	printNode(head);

	bubbleSort(head);

	printNode(head);

	return 0;  
}

void addNode(node* head, int data) {
	node* new_node = (node*)malloc(sizeof(node*));
	new_node->next = head->next;
	head->next = new_node;
	new_node->data = data;
}

void deleteNode(node* head) {
	node* target_node = head->next;
	head->next = target_node->next;
	free(target_node);
}

void bubbleSort(node* head) {
	node* target_node = head->next;
	bool sort_happen = false;
	int temp = -1;
	do {
		sort_happen = false;
		while(target_node->next->next != NULL) {
			if(target_node->data > target_node->next->data) {
				printf("%d target_node->data, %d target_node->next->data changed", target_node->data, target_node->next->data);
				temp = target_node->data;
				target_node->data = target_node->next->data;
				target_node->next->data = temp;
				sort_happen = true;
				printf("\n");
			}
			target_node = target_node->next;
		}
		target_node = head->next;
	} while(sort_happen != false);
}

void printNode(node* head) {
	node* target_node = head->next;
	while(target_node->next != NULL) {
		printf("%d ", target_node->data);
		target_node = target_node->next;
	}
	printf("\n");
}
```
<br>
![Imgur](https://i.imgur.com/gTn2D1R.png)
