#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */

void print_python_string(PyObject *p)
{
	long int length;
	
	fflush(stdout);
	printf("[.] string object info\n");

	/* check if the objevt is string */
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}
	
	/* Retrieve the length of the string */

	length = ((PyASCIIObject *)(p))->length;
	
	
	/* Check if the string is compact ASCII or compact Unicode */

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");
	else
		printf(" type: compact unicode object\n");

	/* Print the length and the wide character representation of the string */
	printf(" length: %d\n", length);
	printf(" value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
