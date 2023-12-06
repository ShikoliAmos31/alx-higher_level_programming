#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
/**
 * print_python_list -This function prints various details about a Python list,
 * including its size,allocated memory, and the types of its elements
 * @p: A pointer to a PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid argument: not a Python list\n");
		return;
	}
	Py_ssize_t size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: Pointer to the Python bytes object (PyObject *)
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid argument: not a Python bytes object\n");
		return;
	}
	Py_ssize_t size = PyBytes_Size(p);
	char *bytes_data = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes_data);

	printf("  first 10 bytes: ");

	for (Py_ssize_t i = 0; i < size && i < 10; ++i)
	{
		printf("%02hhx", bytes_data[i]);
		if (i < 9)
		{
			printf(" ");
		}
	}
	printf("\n");
}
