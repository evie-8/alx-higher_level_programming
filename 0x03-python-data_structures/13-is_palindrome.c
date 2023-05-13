#include "lists.h"
/**
 * is_palindrome - list is same when reversed
 * @head: holds address of first node
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *p1, *p;
	int i = 0, j = 0, mid;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	ptr = *head;
	p1 = *head;
	while (ptr != NULL)
	{
		ptr = ptr->next;
		i++;
	}
	mid = i / 2;
	while (j < mid)
	{
		p1 = p1->next;
		j++;
	}
	p = reverse(&p1);
	ptr = *head;
	while (ptr != NULL && p != NULL)
	{
		if (ptr->n != p->n)
			return (0);
		ptr = ptr->next;
		p = p->next;
	}
	return (1);
}

/**
 * reverse - reverse linked list
 * @head: contains head node address
 * Return: node
 */
listint_t *reverse(listint_t **head)
{
	listint_t *before, *next, *current;

	if (head == NULL || *head == NULL)
		return (NULL);
	before = NULL;
	next = *head;
	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = before;
		before = current;
		current = next;
	}
	*head = before;
	return (*head);
}
