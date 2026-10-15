"""Mark internal developer API pages, including all autosummary descendants."""

from docutils import nodes


def add_developer_api_warning(app, doctree):
    docname = app.env.docname
    if docname != "developer_api" and not docname.startswith("developer_api/"):
        return
    warning = nodes.warning(classes=["developer-api-warning"])
    warning += nodes.paragraph(text="The stormpy developer API is internal and always subject to change.")
    section = next((child for child in doctree.children if isinstance(child, nodes.section)), doctree)
    position = 1 if section.children and isinstance(section.children[0], nodes.title) else 0
    section.insert(position, warning)


def setup(app):
    app.connect("doctree-read", add_developer_api_warning)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
