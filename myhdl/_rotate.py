""" module with the rotate_left and rotate_right functions

"""
from __future__ import absolute_import

from myhdl._compat import integer_types
from myhdl._intbv  import intbv
from myhdl._Signal import _Signal
from myhdl._concat import concat

def rotate_left(value, n):
    
    if isinstance(value, intbv):
        size = value._nrbits
        val  = value._val
    elif isinstance(value, _Signal) and isinstance(value._val, intbv):
        size = value._nrbits
        if isinstance(value._val, intbv):
            val = value._val._val
        else:
            val = value._val
    else:
        raise TypeError("rotate_left: inappropriate first argument type: %s"
                        % type(value))

    if isinstance(n, intbv):
        nVal = n._val
    elif isinstance(n, integer_types):
        nVal = n
    elif isinstance(n, _Signal):
        if isinstance(n._val, intbv):
            nVal = n._val._val
        else:
            nVal = n._val
    elif isinstance(n, str):
        nVal = long(base, 2)
    else:
        raise TypeError("rotate_left: inappropriate second argument type: %s"
                        % type(value))

    mid  = size - nVal

    return concat(val[mid:0], val[size:mid])

def rotate_right(value, n):
    if isinstance(value, intbv):
        size = value._nrbits
        val  = value._val
    elif isinstance(value, _Signal) and isinstance(value._val, intbv):
        size = value._nrbits
        if isinstance(value._val, intbv):
            val = value._val._val
        else:
            val = value._val
    else:
        raise TypeError("rotate_right: inappropriate first argument type: %s"
                        % type(value))

    if isinstance(n, intbv):
        nVal = n._val
    elif isinstance(n, integer_types):
        nVal = n
    elif isinstance(n, _Signal):
        if isinstance(n._val, intbv):
            nVal = n._val._val
        else:
            nVal = n._val
    elif isinstance(n, str):
        nVal = long(base, 2)
    else:
        raise TypeError("rotate_right: inappropriate second argument type: %s"
                        % type(value))

    mid = nVal

    return concat(val[mid:0], val[size:mid])
