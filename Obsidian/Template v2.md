## 📝 Annotations
{% persist "annotations" %}
{% if annotations.length > 0 %}
### Imported on {{importDate | format("YYYY-MM-DD HH:mm")}}
{# 1. Define the desired order of colors and their corresponding headers #}
{% set colorOrder = [
  {name: "yellow", header: "🟡 Introduction & Motivation"},
  {name: "orange", header: "🟠 Constraints"},
  {name: "blue", header: "🔵 Other Papers"},
  {name: "red", header: "🔴 Shortcomings / Critical"},
  {name: "green", header: "🟢 Results & Key Findings"}
] %}
{# 2. Loop through the predefined order of colors #}
{% for color in colorOrder %}
{# 3. Check if any annotations exist for the current color before printing the header #}
{% set matchingAnnotations = annotations | filterby("colorCategory", color.name) %}
{% if matchingAnnotations.length > 0 %}
#### {{ color.header }}
{# 4. Loop through only the annotations that match the current color #}
{% for a in matchingAnnotations | sort(false, false, "pageLabel") %}
> {{a.annotatedText}} [p.{{a.pageLabel}}](zotero://open-pdf/library/items/{{a.attachment.itemKey}}?page={{a.pageLabel}}&annotation={{a.id}})
{% if a.comment %}
> [!NOTE] User Comment
> **{{a.comment}}**
{% endif %}
{% endfor %}
---
{% endif %}
{% endfor %}
{% endif %}
{% endpersist %}