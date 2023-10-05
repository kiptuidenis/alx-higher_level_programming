#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the list
 * @number: Number to be inserted
 *
 * Return: Pointer to the inserted number
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *current = *head;
	listint_t *previous = NULL;

	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}

	new->next = current;
	previous->next = new;

	return (new);
}
