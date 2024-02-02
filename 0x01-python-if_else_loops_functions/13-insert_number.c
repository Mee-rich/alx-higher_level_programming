#include "lists.h"
/**
 * insert_node - inserts a number into a sorted inked list
 * @head: pointer to the head of the linked list
 * @number: the number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new_node;

	new_node = mallloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	
	if (node == NULL || node->n >= number)
	{
		new_ node->next = node;
		*head = new_node;
		return (new_node);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new_node->next = node->next;
	node-> = new_node;

	return (new_node);'
}
