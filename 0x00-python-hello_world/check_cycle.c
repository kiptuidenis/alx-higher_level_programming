#include <stdio.h>
#include <stdlib.h>

/* Define the structure for a singly linked list node */
struct listint_t {
    int data;
    struct listint_t *next;
};

typedef struct listint_t listint_t;

int check_cycle(listint_t *list) {
    listint_t *slow = list;
    listint_t *fast = list;

    if (list == NULL) {
        return 0;  /* No cycle in an empty list */
    }

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;      /* Move one step at a time */
        fast = fast->next->next; /* Move two steps at a time */

        if (slow == fast) {
            return 1; /* Cycle detected */
        }
    }

    return 0; /* No cycle found */
}

int main() {
    listint_t *head = malloc(sizeof(listint_t));
    int hasCycle = check_cycle(head);
    head->data = 1;
    head->next = malloc(sizeof(listint_t));
    head->next->data = 2;
    head->next->next = malloc(sizeof(listint_t));
    head->next->next->data = 3;
    head->next->next->next = head; /* Create a cycle */

    if (hasCycle) {
        printf("The linked list has a cycle.\n");
    } else {
        printf("The linked list does not have a cycle.\n");
    }

    /* Clean up the memory */
    free(head->next->next);
    free(head->next);
    free(head);

    return 0;
}

