#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *next;
	listint_t *first_half, *second_half;

	slow = fast = *head;
	prev = NULL;
	if (*head == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	while (slow != NULL)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	first_half = *head;
	second_half = prev;
	while (second_half)
	{
		if (first_half->n != second_half->n)
			return (0);
		first_half = first_half->next;
		second_half = second_half->next;
	}
	return (1);
}
