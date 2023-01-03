#include "lists.h"

/**
* check_cycle - function checks if a singly linked list has a cycle in it.
* @list: pointer to the beginning of the node
* Return: 0 if no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *node1, *node2;

	if (list == NULL || list->next == NULL)
		return (0);
	node1 = list;
	node2 = node1->next;

	while (node1 != NULL &&
		node2->next != NULL &&
		node2->next->next != NULL)
	{
		if (node1 == node2)
			return (1);
		node1 = node1->next;
		node2 = node2->next->next;
	}
	return (0);
}
