#include "lists.h"

/**
 * check_cycle - checks if the list has a cycle
 * @list: the list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *lion;
	listint_t *cat;

	if (list == NULL || list->next == NULL)
		return (0);

	lion = list;
	cat = list;
	while (cat != NULL && cat->next != NULL)
	{
		lion = lion->next;
		cat = cat->next;
		if (lion == cat)
			return (1);
	}
	return (0);
}
