"""Public constructors for symbolic expressions."""

from stormpy.developer import storage as _bindings


def _plus(lhs, rhs):
    """Construct the sum of two expressions.

    :param lhs: Left operand.
    :param rhs: Right operand.
    :return: Sum expression.
    """
    return lhs + rhs


def _minus(lhs, rhs):
    """Construct the difference of two expressions.

    :param lhs: Left operand.
    :param rhs: Right operand.
    :return: Difference expression.
    """
    return lhs - rhs


def _multiply(lhs, rhs):
    """Construct the product of two expressions.

    :param lhs: Left operand.
    :param rhs: Right operand.
    :return: Product expression.
    """
    return lhs * rhs


def _divide(lhs, rhs):
    """Construct the quotient of two expressions.

    :param lhs: Numerator expression.
    :param rhs: Denominator expression.
    :return: Quotient expression.
    """
    return lhs / rhs


def _and(lhs, rhs):
    """Construct the conjunction of two expressions.

    :param lhs: Left Boolean operand.
    :param rhs: Right Boolean operand.
    :return: Conjunction expression.
    """
    return lhs & rhs


def _or(lhs, rhs):
    """Construct the disjunction of two expressions.

    :param lhs: Left Boolean operand.
    :param rhs: Right Boolean operand.
    :return: Disjunction expression.
    """
    return lhs | rhs


def _geq(lhs, rhs):
    """Construct a greater-than-or-equal comparison.

    :param lhs: Left operand.
    :param rhs: Right operand.
    :return: Boolean comparison expression.
    """
    return lhs >= rhs


def _eq(lhs, rhs):
    """Construct an equality comparison.

    :param lhs: Left operand.
    :param rhs: Right operand.
    :return: Boolean comparison expression.
    """
    return lhs == rhs


def _neq(lhs, rhs):
    """Construct an inequality comparison.

    :param lhs: Left operand.
    :param rhs: Right operand.
    :return: Boolean comparison expression.
    """
    return lhs != rhs


def _greater(lhs, rhs):
    """Construct a greater-than comparison.

    :param lhs: Left operand.
    :param rhs: Right operand.
    :return: Boolean comparison expression.
    """
    return lhs > rhs


def _less(lhs, rhs):
    """Construct a less-than comparison.

    :param lhs: Left operand.
    :param rhs: Right operand.
    :return: Boolean comparison expression.
    """
    return lhs < rhs


def _leq(lhs, rhs):
    """Construct a less-than-or-equal comparison.

    :param lhs: Left operand.
    :param rhs: Right operand.
    :return: Boolean comparison expression.
    """
    return lhs <= rhs


def _modulo(lhs, rhs):
    """Construct the remainder of dividing two expressions.

    :param lhs: Dividend expression.
    :param rhs: Divisor expression.
    :return: Remainder expression.
    """
    return _bindings.modulo(lhs, rhs)


def _implies(lhs, rhs):
    """Construct a logical implication.

    :param lhs: Premise expression.
    :param rhs: Conclusion expression.
    :return: Implication expression.
    """
    return _bindings.implies(lhs, rhs)


def _iff(lhs, rhs):
    """Construct a logical equivalence.

    :param lhs: Left Boolean operand.
    :param rhs: Right Boolean operand.
    :return: Equivalence expression.
    """
    return _bindings.iff(lhs, rhs)


def _conjunction(expressions):
    """Construct the conjunction of a collection of expressions.

    :param expressions: Non-empty iterable of Boolean expressions.
    :return: Conjunction expression.
    """
    return _bindings.conjunction(list(expressions))


def _disjunction(expressions):
    """Construct the disjunction of a collection of expressions.

    :param expressions: Non-empty iterable of Boolean expressions.
    :return: Disjunction expression.
    """
    return _bindings.disjunction(list(expressions))


_bindings.Expression.Plus = staticmethod(_plus)
_bindings.Expression.Minus = staticmethod(_minus)
_bindings.Expression.Multiply = staticmethod(_multiply)
_bindings.Expression.Divide = staticmethod(_divide)
_bindings.Expression.And = staticmethod(_and)
_bindings.Expression.Or = staticmethod(_or)
_bindings.Expression.Geq = staticmethod(_geq)
_bindings.Expression.Eq = staticmethod(_eq)
_bindings.Expression.Neq = staticmethod(_neq)
_bindings.Expression.Greater = staticmethod(_greater)
_bindings.Expression.Less = staticmethod(_less)
_bindings.Expression.Leq = staticmethod(_leq)
_bindings.Expression.Modulo = staticmethod(_modulo)
_bindings.Expression.Implies = staticmethod(_implies)
_bindings.Expression.Iff = staticmethod(_iff)
_bindings.Expression.Conjunction = staticmethod(_conjunction)
_bindings.Expression.Disjunction = staticmethod(_disjunction)
