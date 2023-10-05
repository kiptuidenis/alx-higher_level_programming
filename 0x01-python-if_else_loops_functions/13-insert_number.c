#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: points to head of list
 * @number: number to be inserted
 *
 * Return: pointer to inserted number
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *ahead;
	listint_t *behind;

	behind = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (*head == NULL)
	{
		*head = new;
		new->n = number;
		return (new);
	}
	if (behind->n >= number)
	{
		*head = new;
		new->next = behind;
		return (new);
	}
	else
	{
		ahead = behind->next;
		while (ahead != NULL)
		{
			if (ahead->n >= number)
			{
				new->next = ahead;
				new->n = number;
				behind->next = new;
				return (new);
			}
			ahead = ahead->next;
			behind = behind->next;
		}
		new = add_nodeint_end(head, number);
		return (new);
	}
}
