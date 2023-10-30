#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - a singly linked list structure
 * @n: initialized integer
 * @next: pointer to the next node
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
int check_cycle(listint_t *list);
listint_t *add_nodeint(listint_t **head, const int n);

#endif /* LISTS_H */
