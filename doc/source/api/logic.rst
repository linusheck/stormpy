Stormpy.logic
*************

``stormpy.logic`` contains the formula classes used to represent properties.

Base classes
============

.. autosummary::
   :toctree: generated/logic
   :template: autosummary/class.rst

   stormpy.logic.Formula
   stormpy.logic.StateFormula
   stormpy.logic.PathFormula
   stormpy.logic.UnaryStateFormula
   stormpy.logic.BinaryStateFormula
   stormpy.logic.UnaryPathFormula
   stormpy.logic.BinaryPathFormula

Atomic and Boolean formulas
===========================

.. autosummary::
   :toctree: generated/logic
   :template: autosummary/class.rst

   stormpy.logic.AtomicExpressionFormula
   stormpy.logic.AtomicLabelFormula
   stormpy.logic.BooleanLiteralFormula
   stormpy.logic.UnaryBooleanStateFormula
   stormpy.logic.BooleanBinaryStateFormula

Path formulas
=============

.. autosummary::
   :toctree: generated/logic
   :template: autosummary/class.rst

   stormpy.logic.EventuallyFormula
   stormpy.logic.GloballyFormula
   stormpy.logic.UntilFormula
   stormpy.logic.BoundedUntilFormula
   stormpy.logic.ConditionalFormula

Operator formulas
=================

.. autosummary::
   :toctree: generated/logic
   :template: autosummary/class.rst

   stormpy.logic.OperatorFormula
   stormpy.logic.ProbabilityOperator
   stormpy.logic.RewardOperator
   stormpy.logic.TimeOperator
   stormpy.logic.LongRunAvarageOperator
   stormpy.logic.MultiObjectiveFormula
   stormpy.logic.GameFormula

Reward formulas
===============

.. autosummary::
   :toctree: generated/logic
   :template: autosummary/class.rst

   stormpy.logic.CumulativeRewardFormula
   stormpy.logic.InstantaneousRewardFormula
   stormpy.logic.LongRunAverageRewardFormula

Enumerations
============

.. autosummary::
   :toctree: generated/logic
   :template: autosummary/class.rst

   stormpy.logic.ComparisonType
   stormpy.logic.BinaryBooleanOperatorType
