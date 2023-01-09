import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
lib_some = ['hello', 'World']
lib.print_python_list_info(lib_some)
del lib_some[1]
lib.print_python_list_info(lib_some)
lib_some = lib_some + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(lib_some)
lib_some = []
lib.print_python_list_info(lib_some)
lib_some.append(0)
lib.print_python_list_info(lib_some)
lib_some.append(1)
lib_some.append(2)
lib_some.append(3)
lib_some.append(4)
lib.print_python_list_info(lib_some)
lib_some.pop()
lib.print_python_list_info(lib_some)
