#include <stdio.h>
#include <Python.h>

void print_python_string(PyObject *p) {
    // Check if the object is a string
    if (PyUnicode_Check(p)) {
        // Extract the string from the Python object
        const char *str = PyUnicode_AsUTF8(p);

        // Check if the conversion was successful
        if (str != NULL) {
            // Print the string
            printf("String: %s\n", str);
        } else {
            // Handle conversion error
            fprintf(stderr, "Error: Unable to convert Python string to UTF-8\n");
        }
    } else {
        // Handle error when the object is not a valid string
        fprintf(stderr, "Error: Not a valid Python string\n");
    }
}

// Example usage
int main() {
    // Initialize the Python interpreter
    Py_Initialize();

    // Create a Python string object
    PyObject *pyString = PyUnicode_DecodeUTF8("Hello, Python!", strlen("Hello, Python!"), "strict");

    // Print the Python string
    print_python_string(pyString);

    // Clean up
    Py_XDECREF(pyString);
    Py_Finalize();

    return 0;
}
