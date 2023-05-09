#include "lists.h"
#include "stdlib.h"
/**
 * insert_node - insert node
 * @head: pointer
 * @number: where to insert
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *ptr;
	int i = 0;

	if (head == NULL)
		return (NULL);
	ptr = *head;
	if (ptr == NULL)
	{
		new = insert_nodeint_at_index(head, i, number);
		return (new);
	}
	while (ptr != NULL)
	{
		if (ptr->n >= number)
		{
			new = insert_nodeint_at_index(head, i, number);
			return (new);
		}
		else if (ptr->next == NULL && ptr->n <= number)
		{
			new = insert_nodeint_at_index(head, i + 1, number);
			return (new);
		}
		else
			ptr = ptr->next;
		i++;
	}
	return (NULL);
}
/**
 * insert_nodeint_at_index - inset node at specified index
 * @head: pointer to a listint_t pointer
 * @idx: node position
 * @n: data
 * Return: node
 */
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
	listint_t *p, *ptr;
	unsigned int x;

	p = malloc(sizeof(listint_t));
	if (p == NULL)
		return (NULL);
	p->n = n;
	p->next = NULL;
	ptr = *head;

	if (idx == 0)
	{
		p->next = ptr;
		*head = p;
		return (p);
	}
	x = 0;
	while (x < idx - 1)
	{
		if (ptr == NULL || ptr->next == NULL)
			return (NULL);
		ptr = ptr->next;
		x++;
	}
	p->next = ptr->next;
	ptr->next = p;
	return (p);
}
