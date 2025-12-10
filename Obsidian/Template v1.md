## 📝 Annotations

{% persist "annotations" %}
{% set annotations = annotations | sort(false, false, "pageLabel") %}

{% if annotations.length > 0 %}
### Imported on {{importDate | format("YYYY-MM-DD HH:mm")}}

{% for a in annotations %}


{% if a.colorCategory == "Yellow" %}
#### 🟡 Introduction & Motivation
{% elif a.colorCategory == "Red" %}
#### 🔴 Shortcomings / Critique
{% elif a.colorCategory == "Green" %}
#### 🟢 Results & Key Findings
{% elif a.colorCategory == "Blue" %}
#### 🔵 Other studies found
{% elif a.colorCategory == "orange" %}
####  🟠 Constraints
{% endif %}

> {{a.annotatedText}} [p.{{a.pageLabel}}](zotero://open-pdf/library/items/{{a.attachment.itemKey}}?page={{a.pageLabel}}&annotation={{a.id}})

{% if a.comment %}
> [!NOTE] User Comment
> **{{a.comment}}**
{% endif %}


{% endfor %}
{% endif %}
{% endpersist %}