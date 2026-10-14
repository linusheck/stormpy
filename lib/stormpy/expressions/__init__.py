"""Symbolic expressions, variables and expression parsing.

An ``ExpressionManager`` owns the variables used in a model description.
Declare them with ``declare_boolean_variable``, ``declare_integer_variable``,
``declare_rational_variable`` or ``declare_string_variable``. Their
``get_expression()`` methods produce expressions which can be combined using
``Expression`` operators. Constants are created with the manager's ``boolean``,
``integer`` and ``rational`` methods. The ``create_*`` spellings are public
Python conveniences for the same operations.

``ExpressionParser(manager)`` parses expressions using that manager's variables.
``ExpressionType`` and ``OperatorType`` describe expression types and operators.
Expression variables are distinct from the rational-function parameters in
``stormpy.numbers``.

The raw Storm bindings are available in :mod:`stormpy.developer.storage`."""

from stormpy.developer import storage as _bindings

ExpressionManager = _bindings.ExpressionManager
Expression = _bindings.Expression
Variable = _bindings.Variable
ExpressionParser = _bindings.ExpressionParser
ExpressionType = _bindings.ExpressionType
OperatorType = _bindings.OperatorType

__all__ = ["ExpressionManager", "Expression", "Variable", "ExpressionParser", "ExpressionType", "OperatorType"]

from . import _convenience
