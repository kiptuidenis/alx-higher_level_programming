#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/* Define the structure for a singly linked list node */
struct listint_t {
    int data;
    struct listint_t *next;
};


typedef struct listint_t listint_t;


int check_cycle(listint_t *list);

#endif
