#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - this function checks if a singly linked list has a cycle
 * @list: list to be checked
 * Return: 1 if there is a cycle or 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *temp;
	int n = 0;

	temp = head;
	while (temp != NULL)
	{
		temp = temp->next;
		if (temp == head)
			break;
		n++;
	}
	if (temp == head && n >= 1)
		return (1);
	return (0);
}
