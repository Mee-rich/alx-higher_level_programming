#include "lists.h"
/**
 * list_reverse - c function that checks if a 
 * 		singly linked list is a palindrome.
 * @head: pointer to the first node
 *
 * Return: pointer to the new node first node
 */
void list_reverse(listint_t **head)
{
	listint_t *old = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;
	
	while (curr)
	{
		next = curr->next;
		curr->next = old;
		old = curr;
		curr = next;
	}
	*head = old;
}

 /**
 * is_palindrome - checks if a singly 
 * 		linked list is a palindrome.
 * @head: the pointer to the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *dub = NULL;
	listint_t *slow = *head, *fast = *head;
	
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dub = slow->next;
			break;
		}
		if (!fast->next)
		{
			dub = slow->next->next;
			bread;
		}
		slow = slow->next;
	}

	
	list_reverse(&dub);
	while (dub && tmp)
	{
		if (tmp->n == dub->n)
		{
			dub = dub->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}

	if (!dub)
		return (1);
	return (0);
}

