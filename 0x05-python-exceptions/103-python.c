#include <Python.h>
/**
 * print_python_list -function that prints python list
 * @p: object to be printed
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Python list info\n  [ERROR] Invalid List Object\n");
		return;
	}
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *element = PyList_GetItem(p, i);

		printf("Element %zd: ", i);

		if (PyBytes_Check(element))
		{
			print_python_bytes(element);
		}
		else if (PyFloat_Check(element))
		{
			print_python_float(element);
		}
		else if (PyLong_Check(element))
		{
			printf("int\n");
		}
		else if (PyTuple_Check(element))
		{
			printf("tuple\n");
		}
		else if (PyList_Check(element))
		{
			print_python_list(element);
		}
		else if (PyUnicode_Check(element))
		{
			printf("str\n");
		}
	}
}
/**
 * print_python_bytes -that prints python in bytes
 * @p: bytes to be printed
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
		return;
	}
	Py_ssize_t size = PyBytes_Size(p);
	char *str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %zd bytes: ", size > 10 ? 10 : size);

	for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); ++i)
	{
		printf("%02x ", (unsigned char)str[i]);
	}
	printf("\n");
}
/**
 * print_python_float -that prints float in python
 * @p: float to be printed
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[.] float object info\n  [ERROR] Invalid Float Object\n");
		return;
	}
	double value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %lf\n", value);
}
