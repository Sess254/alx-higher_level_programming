/*
 *File: 10-check_cyle.c
 *Auth: Sess254
 */

#include "lists.h"

/**
 * check_cycle - checks if a singly-linked list has a cycle
 *@list: singly-linked list
 *
 *Return: if no cycle - 0, if cycle 1
 */

int check_cycle(listint_t *list)
{
	listint_t *c, *n;

	if (list == NULL || list->next == NULL)
		return (0);

	c = list;
	n = c->next;

	while (c && n->next && n->next->next)
	{
		if (c == n)
			return (1);

		c = c->next;
		n = n->next->next;
	}

	return (0);
}
