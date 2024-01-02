#include "lists.h"

/**
 * check_cycle - check for loop in linked list
 * @list: head of linked list
 *
 * Description - check for loop in linked list
 * Return: 1 if cycled, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *hill, *valley;

	if (!list)
		return (0);
	valley = list;
	hill = list->next;
	while (valley && hill && hill->next)
	{
		if (valley == hill)
		{
			return (1);
		}
		valley = valley->next;
		hill = hill->next->next;
	}
	return (0);
}
