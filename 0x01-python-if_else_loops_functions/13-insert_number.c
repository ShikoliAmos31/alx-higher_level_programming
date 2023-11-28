#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <unistd.h>

/**
 * insert_node -function that inserts a number into a
 * sorted singly linked list in C
 * @number: number to be inserted
 * @head: the linked list
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *temp, *new = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n < number)
		{
			temp = current;
			current = current->next;
		}
		temp->next = new;
		new->next = current;
	}
	return (new);
}
