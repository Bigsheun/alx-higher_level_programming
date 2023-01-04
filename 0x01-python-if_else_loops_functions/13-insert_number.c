#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
* insert_node - inserts a node
* @head: head
* @number: int to add
* Return: new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL, *node = NULL;

	if (head == NULL)
		return (NULL);

	node = malloc(sizeof(listint_t *));
	if (node == NULL)
		return (NULL);

	node->n = number;

	temp = *head;
	if (temp == NULL || temp->n >= number)
	{
		node->next = temp;
		head[0] = node;
		return (node);
	}


	while (temp->next != NULL && temp->next->n < number)
		temp = temp->next;


	node->next = temp->next;
	temp->next = node;

	return (node);
}
