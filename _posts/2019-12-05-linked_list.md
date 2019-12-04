---
layout: post
title: "What's a Linked List"
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

This post is for the very beginner.

Linked list is quiet good example to explain struct, pointer and memory.

Let's think about when we stand in line.

[Imgur](https://i.imgur.com/sCP6WZD.jpg)

We usually don't know what order i'm standing in at the front. However we know who stand just in front us.
Like this, let's guess we are a "NODE", we have two information. First one is the person who stand in front us.
Second one is a data like height. so we can write code like this

typedef struct NODE {
  struct NODE* next; // Point out next struct *memory address* **using pointer( * )**
  int data; // Store a data like height
}node; // define this kind of NODE struct as "node"


"struct NODE* next"
All the data has a memory address to stored.
*struct NODE next* replaced NODE* cause error because it is trying that define the same struct in the struct.
To have information for next person, We should point out memory address of next NODE.

[Imgur](https://i.imgur.com/QT6yFfn.jpg)

a woman wearing backpack also has information for next and data.

From the void, we need to reference point.


node* head = (node*)malloc(sizeof(node*)); // dynamically allocate memory size as much as node* structure. it returns memory address.
node* tail = (node*)malloc(sizeof(node*));

head->next = tail; // tail is head->next
tail->next = NULL; // NULL is tail->next

**pointer** is used to point out *memory address* so we need to dynamically allocate memory.

####**=**
A = B is meaning that put B data to A. B is A.


void addNode(node* head, int data) {
	node* new_node = (node*)malloc(sizeof(node*)); // Make a new node to add
	new_node->next = head->next; // new node next point out the point that head pointed.
	head->next = new_node; // head point out the new node
	new_node->data = data;
}


Let's think that someone cut in line.
someone is coming.
this guy stand behind the woman wearing the backpack.
Now I am standing behind the bad guy.


void deleteNode(node* head) {
	node* target_node = head->next; // point out node next to head
	head->next = target_node->next;
	free(target_node); // free the momory
}


Let's point out someone in front of me.
the guy in front of other guy will be the one that in front of me.
he will leave from the line.


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


Bubblesort is one of the sorting. We will take a look later.
Let's think that stand in the line follow the height order.
Bubblesort is comparison that 1:1 comparing to data, if I'm taller than next person, change the position.
After one cycle, the tallest one is stand the first of the line.
We repeat sorting until there is no change the position.


void printNode(node* head) {
	node* target_node = head->next; // point out the node next to head
	while(target_node->next != NULL) {
		printf("%d ", target_node->data);
		target_node = target_node->next; // move to the next node
	}
	printf("\n");
}


print the data is traverse the node until tail.


Point of linked list is memory and address.
**" * "** pointer is used to point out address.
If you understand the concept. it would be easy to understand.

Please refer to the full code and test on [IDEONE](https://ideone.com/ideone/Index/submit/)
If you have a question, please leave a comment on the post.

Thank you.


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


[Imgur](https://i.imgur.com/gTn2D1R.png)
