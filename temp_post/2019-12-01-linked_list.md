---
layout: post
title: "What's a Linked List"
description: Explain a linked list.
headline: Let's find out about a Linked list.
modified: 2019-12-01
category: Programming
tags: [C++], [C]
imagefeature:
mathjax:
chart:
comments: true
---

This post is for the very beginner.

Linked list is quiet good example to explain struct, pointer and memory.

Let's think about when we stand in line.

[Imgur](https://i.imgur.com/sCP6WZD.jpg)

We usually don't know what order i'm standing in at the front. However we know who stand just in front us.
Like this, let's guess we are a "NODE", we have two information. First one is the person who stand in front us.
Second one is a data like height. so we can write code like this
---
typedef struct NODE {
  struct NODE* next; // Point out next struct *memory address* **using pointer( * )**
  int data; // Store a data like height
}node; // define this kind of NODE struct as "node"
---

"struct NODE* next"
All the data has a memory address to stored.
*struct NODE next* replaced NODE* cause error because it is trying that define the same struct in the struct.
To have information for next person, We should point out memory address of next NODE.

[Imgur](https://i.imgur.com/QT6yFfn.jpg)

a woman wearing backpack also has information for next and data.


---
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
---

[Imgur](https://i.imgur.com/gTn2D1R.png)
