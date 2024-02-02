#include "hash_tables.h"

/**
 * hash_table_set - function that adds 
 * 	an element to the hash table
 * @ht: the hash table you want to 
 * 	add to or update the key/value to
 * @value: the value associated with the key.
 *
 * Return: 1 if successful otherwise 0
 *	In case of collision add the new 
 *	node at the beginning of the list
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	hash_node_t *new;
	char *value_copy;
	unsigned long int index, i;

	if (ht == NULL || key == NULL || *key == '\0' || value == NULL)
		return (0);
	
	value_copy = strdup(value);

	if (value_copy == NULL)
		return (0);
	index = key_index((const unsigned char *)key, ht->size);
	for ( i = index; ht->array[i]; i++)
	{
		if (strcmp(ht->array[i]->key, key) == 0)
		{
			free(ht->array[i]->value);
			ht->array[i]->value = value_copy;
			return (i);
		}
	}
	
	new = malloc(sizeof(hash_node_t));
	if (new == NULL)
	{
		free(new);
		return (0);
	}
	new->value = value_copy;
	new->next = ht->array[index];
	ht->array[index] = new;

	return (1);
}
