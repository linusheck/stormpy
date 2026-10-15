{% set info = template_function_info(fullname) %}
{{ objname | escape | underline }}

.. currentmodule:: {{ module }}

.. py:function:: {{ objname }}[{{ info.parameters }}](*args, **kwargs)

   Select a specialization with ``{{ objname }}[{{ info.parameters }}](...)``.

   Supported specializations: {% for specialization in info.instantiations %}``{{ specialization }}``{% if not loop.last %}, {% endif %}{% endfor %}.

{% for description, specializations in info.descriptions %}
{% if info.descriptions | length > 1 %}
   For {% for specialization in specializations %}``{{ specialization }}``{% if not loop.last %}, {% endif %}{% endfor %}:
{% endif %}

   .. code-block:: text

{{ description | indent(6, true) }}
{% endfor %}
