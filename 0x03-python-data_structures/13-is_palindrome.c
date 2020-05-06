#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: Double pointer to listint_t single linked list's head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp_beg, *tmp_end;
	int counter1, counter2, c1, c2;

	if (!*head)
		return (1);
	tmp_beg = *head;
	tmp_end = *head;
	counter1 = 0, counter2 = 0;
	while (tmp_end->next)
	{
		counter2++;
		tmp_end = tmp_end->next;
	}
	tmp_end = *head;
	while (counter1 < counter2)
	{
		c1 = 0, c2 = 0;
		while (c1 < counter1)
		{
			tmp_beg = tmp_beg->next;
			c1++;
		}
		while (c2 < counter2)
		{
			tmp_end = tmp_end->next;
			c2++;
		}
		if (tmp_beg->n != tmp_end->n)
			return (0);
		counter1++;
		counter2--;
		tmp_beg = *head;
		tmp_end = *head;
	}
	return (1);
}
