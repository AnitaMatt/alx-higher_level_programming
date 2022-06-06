#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if the list is a palindrome
 * @head: value at head
 * Return: 1 0r 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	long int *my_array;
	int i, n, flag = 0;

	if (temp == NULL)
		return (1);
	while (temp != NULL)
	{
		temp = temp->next;
		n++;
	}
	if (n == 1)
		return (0);
	my_array = malloc(n * sizeof(long int));
	while (temp != NULL && i < n)
	{
		my_array[i] = temp->n;
		temp = temp->next;
		i++;
	}
	if (n % 2 == 0)
		n = n / 2;
	else
	{
		n = n / 2 - 1;
	}
	for (i = 0; i < n; i++)
	{
		if (my_array[i] == my_array[n - 1])
			flag++;
	}
	free(my_array);
	if (flag == i)
		return (1);
	else
		return (0);
}
