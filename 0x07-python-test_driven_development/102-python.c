#include <Python.h>

/**
 * print_python_string - Prints information about Python strings
 * @p: Python object (string)
 */
void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
		printf("[.] string object info\n");

		if (PyUnicode_IS_COMPACT_ASCII(p))
            printf("  type: compact ascii\n");
		else
			printf("  type: compact unicode object\n");

		Py_ssize_t length = PyUnicode_GET_LENGTH(p);
		const char *value = PyUnicode_AsUTF8(p);

		printf("  length: %ld\n", length);
		printf("  value: %s\n", value);
	}
	else
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
	}
}
