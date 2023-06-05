/*
 *File: 10-linked_lists.c
 *Auth: Sess254
 */

#include "lists.h"

/**
 *print_listint - prints elements of a listint_t list
 *@h: pointer to headlist
 *
 *Return: number of the nodes
 */

size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n;

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}
	return (n);
}

/**
 *add_nodeint- adds new node at begining of listint_t list
 *@head: pointer to pointer to the start of the list
 *@n: integer to be in the node
 *
 *Return: address of new element
 *NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
 *free_listint_t - frees a listint_list
 *@head: pointer to the list to be freed
 *
 *Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
