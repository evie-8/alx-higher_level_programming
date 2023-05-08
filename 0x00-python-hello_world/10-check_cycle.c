#include "lists.h"
/**
 * check_cycle - number of cycles
 * @list: nodes
 * Return: 0 if no cycles and 1 if the are cycles
 */
int check_cycle(listint_t *list)
{
	listint_t *f, *s;

	s = list;
	f = list;
	while (s != NULL || f != NULL || f->next != NULL)
	{
		if (s == f)
			return (1);
		s = s->next;
		f = f->next->next;
	}
	return (0);
}
