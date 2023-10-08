#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *second_half;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
/* Reverse the second half of the list. */
		second_half = slow;
		prev_slow->next = NULL;
		reverse_list(&second_half);
/* Compare the first and second halves of the list. */
		while (*head != NULL && second_half != NULL)
		{
			if ((*head)->n != second_half->n)
			{
				is_palindrome = 0;
				break;
			}
			*head = (*head)->next;
			second_half = second_half->next;
		}
		/* Restore the original list. */
		reverse_list(&second_half);
		if (prev_slow)
			prev_slow->next = second_half;
	}
	return (is_palindrome);
}
