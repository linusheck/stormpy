"""Prism and JANI descriptions and UMB archive input/output.

``PrismProgram`` and ``JaniModel`` describe symbolic models before state-space
construction. Their modules, automata, commands, edges, variables and assignments
can be inspected using the corresponding description classes in this package.
Core parsing functions continue to be available through ``stormpy``.

``import_umb`` reads an archive into an intermediate ``UmbModel``. ``to_umb``
converts a sparse model to that representation, and ``umb_to_archive`` writes it
to disk. Use ``stormpy.build_model_from_umb`` to obtain a sparse model directly,
and ``stormpy.export_to_umb`` to export one directly. Import/export options select
numeric encodings, metadata and compression. File wrappers accept strings and
path-like objects, and allocate fresh default options for each call.

``export_jani_to_file`` writes a JANI description and optional properties.

The raw Storm bindings are available in :mod:`stormpy.developer.storage`."""

from stormpy.developer import storage as _bindings

PrismProgram = _bindings.PrismProgram
PrismModule = _bindings.PrismModule
PrismCommand = _bindings.PrismCommand
PrismUpdate = _bindings.PrismUpdate
PrismAssignment = _bindings.PrismAssignment
PrismLabel = _bindings.PrismLabel
PrismModelType = _bindings.PrismModelType
PrismConstant = _bindings.PrismConstant
PrismVariable = _bindings.PrismVariable
PrismIntegerVariable = _bindings.PrismIntegerVariable
PrismBooleanVariable = _bindings.PrismBooleanVariable
PrismRewardModel = _bindings.PrismRewardModel
JaniModel = _bindings.JaniModel
JaniAutomaton = _bindings.JaniAutomaton
JaniEdge = _bindings.JaniEdge
JaniTemplateEdge = _bindings.JaniTemplateEdge
JaniEdgeDestination = _bindings.JaniEdgeDestination
JaniTemplateEdgeDestination = _bindings.JaniTemplateEdgeDestination
JaniOrderedAssignments = _bindings.JaniOrderedAssignments
JaniAssignment = _bindings.JaniAssignment
JaniLocation = _bindings.JaniLocation
JaniVariableSet = _bindings.JaniVariableSet
JaniType = _bindings.JaniType
BasicType = _bindings.BasicType
BoundedType = _bindings.BoundedType
ClockType = _bindings.ClockType
ArrayType = _bindings.ArrayType
ContinuousType = _bindings.ContinuousType
JaniVariable = _bindings.JaniVariable
JaniConstant = _bindings.JaniConstant
CompressionMode = _bindings.CompressionMode
UmbImportValueType = _bindings.UmbImportValueType
UmbImportOptions = _bindings.UmbImportOptions
UmbExportValueType = _bindings.UmbExportValueType
UmbExportOptions = _bindings.UmbExportOptions
UmbModel = _bindings.UmbModel

__all__ = [
    "PrismProgram",
    "PrismModule",
    "PrismCommand",
    "PrismUpdate",
    "PrismAssignment",
    "PrismLabel",
    "PrismModelType",
    "PrismConstant",
    "PrismVariable",
    "PrismIntegerVariable",
    "PrismBooleanVariable",
    "PrismRewardModel",
    "JaniModel",
    "JaniAutomaton",
    "JaniEdge",
    "JaniTemplateEdge",
    "JaniEdgeDestination",
    "JaniTemplateEdgeDestination",
    "JaniOrderedAssignments",
    "JaniAssignment",
    "JaniLocation",
    "JaniVariableSet",
    "JaniType",
    "BasicType",
    "BoundedType",
    "ClockType",
    "ArrayType",
    "ContinuousType",
    "JaniVariable",
    "JaniConstant",
    "CompressionMode",
    "UmbImportValueType",
    "UmbImportOptions",
    "UmbExportValueType",
    "UmbExportOptions",
    "UmbModel",
]


def import_umb(path, *, options=None):
    """Read a UMB archive into an intermediate UMB model.

    :param path: Archive filename as a string or path-like object.
    :param options: Optional UmbImportOptions controlling imported values and metadata.
    :return: The intermediate UmbModel; use build_model_from_umb to build a sparse model.
    """
    from stormpy.core._common import _path

    return _bindings.import_umb(_path(path), options if options is not None else UmbImportOptions())


def umb_to_archive(umb_model, path, options=None):
    """Write an intermediate UMB model to an archive.

    :param umb_model: UMB model to export.
    :param path: Archive filename as a string or path-like object.
    :param options: Optional UmbExportOptions controlling values and compression.
    """
    from stormpy.core._common import _path

    _bindings.to_archive(umb_model, _path(path), options if options is not None else UmbExportOptions())


def export_jani_to_file(filename, model, properties=None, *, check_valid=True, compact=False):
    """Write a JANI model and its properties as JSON.

    :param filename: Output filename as a string or path-like object.
    :param model: JANI model to export.
    :param properties: Optional iterable of properties to include.
    :param check_valid: Whether to validate the model before exporting it.
    :param compact: Whether to omit JSON indentation.
    """
    from stormpy.core._common import _path

    _bindings.JsonExporter.to_file(model, list(properties) if properties is not None else [], _path(filename), check_valid, compact)


__all__ += ["import_umb", "umb_to_archive", "export_jani_to_file"]


def to_umb(model, *, options=None):
    """Convert a sparse model to the intermediate UMB representation.

    :param model: Sparse model with floating point, exact or interval values.
    :param options: Optional UmbExportOptions controlling output value encoding.
    :return: Intermediate UmbModel for inspection or archive export.
    """
    return _bindings.sparse_model_to_umb(model, options if options is not None else UmbExportOptions())


__all__ += ["to_umb"]

from . import _convenience
