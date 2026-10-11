"""Export of models into explicit file formats."""

from __future__ import annotations

from stormpy import developer, storage
from stormpy.developer import DirectEncodingExporterOptions


def export_to_drn(model, path: str, *, options: DirectEncodingExporterOptions | None = None) -> None:
    """
    Export a sparse model in the explicit DRN format.

    :param model: Sparse model.
    :param path: Path of the output file.
    :param options: (optional) Options for the exporter.
    """
    developer.export_sparse_model_as_drn(model, path, options if options is not None else DirectEncodingExporterOptions())


def export_to_umb(model, path: str, *, options: storage.UmbExportOptions | None = None) -> None:
    """
    Export a sparse model as UMB archive.

    :param model: Sparse model.
    :param path: Path of the output archive.
    :param options: (optional) Options controlling the value type, compression, etc.
    """
    options = options if options is not None else storage.UmbExportOptions()
    umb = storage.sparse_model_to_umb(model, options)
    storage.umb_to_archive(umb, path, options)
