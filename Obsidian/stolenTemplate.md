---
title: "{{title}}"
{% if date %}year: {{date | format("YYYY")}}{% endif %}
author_links: {% for author in authors %}[["{{author.firstName}} {{author.lastName}}"]]{% if not loop.last %}, {% endif %}{% endfor %}
zotero_citekey: {{citekey}}
aliases: ["{{citekey}}"]
tags: 
  - zotero 
---

{{ bibliography }}

- [Open in Zotero]({{desktopURI}})
- url: {{url}}
{% if pdfLink -%}
- [Open PDF]({{pdfLink}})
{%- endif -%}

{% if abstractNote %}
# Abstract
{{ abstractNote }}
{% endif %}

# Highlights

## Introduction / Motivation
{% for annotation in annotations %}{% if annotation.color == "#ffd400" %}
{% if annotation.annotatedText %}
> [!cite]
> {{annotation.annotatedText}}
> [Page {{annotation.pageLabel}}]({{annotation.desktopURI}})
{%- if annotation.comment %}
> > [!note]
> > {{annotation.comment}}
{% endif %}
{% else %}{% if annotation.comment %}
> [!note]
> {{annotation.comment}}
> [Page {{annotation.pageLabel}}]({{annotation.desktopURI}})
{% endif -%}{% endif -%}
{% if annotation.imageRelativePath %}
![[{{annotation.imageRelativePath}}]]
{% endif -%}
{% endif %}{% endfor %}

## Methodology
{% for annotation in annotations %}{% if annotation.color == "#a28ae5" %}
{% if annotation.annotatedText %}
> [!cite]
> {{annotation.annotatedText}}
> [Page {{annotation.pageLabel}}]({{annotation.desktopURI}})
{%- if annotation.comment %}
> > [!note]
> > {{annotation.comment}}
{% endif %}
{% else %}{% if annotation.comment %}
> [!note]
> {{annotation.comment}}
> [Page {{annotation.pageLabel}}]({{annotation.desktopURI}})
{% endif -%}{% endif -%}
{% if annotation.imageRelativePath %}
![[{{annotation.imageRelativePath}}]]
{% endif -%}
{% endif %}{% endfor %}

## General Shortcomings
{% for annotation in annotations %}{% if annotation.color == "#ff6666" %}
{% if annotation.annotatedText %}
> [!cite]
> {{annotation.annotatedText}}
> [Page {{annotation.pageLabel}}]({{annotation.desktopURI}})
{%- if annotation.comment %}
> > [!note]
> > {{annotation.comment}}
{% endif %}
{% else %}{% if annotation.comment %}
> [!note]
> {{annotation.comment}}
> [Page {{annotation.pageLabel}}]({{annotation.desktopURI}})
{% endif -%}{% endif -%}
{% if annotation.imageRelativePath %}
![[{{annotation.imageRelativePath}}]]
{% endif -%}
{% endif %}{% endfor %}

## Results of Study
{% for annotation in annotations %}{% if annotation.color == "#5fb236" %}
{% if annotation.annotatedText %}
> [!cite]
> {{annotation.annotatedText}}
> [Page {{annotation.pageLabel}}]({{annotation.desktopURI}})
{%- if annotation.comment %}
> > [!note]
> > {{annotation.comment}}
{% endif %}
{% else %}{% if annotation.comment %}
> [!note]
> {{annotation.comment}}
> [Page {{annotation.pageLabel}}]({{annotation.desktopURI}})
{% endif -%}{% endif -%}
{% if annotation.imageRelativePath %}
![[{{annotation.imageRelativePath}}]]
{% endif -%}
{% endif %}{% endfor %}

## Other Studies Findings
{% for annotation in annotations %}{% if annotation.color == "#2ea8e5" %}
{% if annotation.annotatedText %}
> [!cite]
> {{annotation.annotatedText}}
> [Page {{annotation.pageLabel}}]({{annotation.desktopURI}})
{%- if annotation.comment %}
> > [!note]
> > {{annotation.comment}}
{% endif %}
{% else %}{% if annotation.comment %}
> [!note]
> {{annotation.comment}}
> [Page {{annotation.pageLabel}}]({{annotation.desktopURI}})
{% endif -%}{% endif -%}
{% if annotation.imageRelativePath %}
![[{{annotation.imageRelativePath}}]]
{% endif -%}
{% endif %}{% endfor %}

## Constraints
{% for annotation in annotations %}{% if annotation.color == "#f19837" %}
{% if annotation.annotatedText %}
> [!cite]
> {{annotation.annotatedText}}
> [Page {{annotation.pageLabel}}]({{annotation.desktopURI}})
{%- if annotation.comment %}
> > [!note]
> > {{annotation.comment}}
{% endif %}
{% else %}{% if annotation.comment %}
> [!note]
> {{annotation.comment}}
> [Page {{annotation.pageLabel}}]({{annotation.desktopURI}})
{% endif -%}{% endif -%}
{% if annotation.imageRelativePath %}
![[{{annotation.imageRelativePath}}]]
{% endif -%}
{% endif %}{% endfor %}

## Other Annotations
{% for annotation in annotations %}{% if annotation.color != "#ffd400" and annotation.color != "#ff6666" and annotation.color != "#5fb236" and annotation.color != "#2ea8e5" and annotation.color != "#f19837" and annotation.color != "#a28ae5" %}
{% if annotation.annotatedText %}
> [!cite]
> {{annotation.annotatedText}}
> [Page {{annotation.pageLabel}}]({{annotation.desktopURI}})
{%- if annotation.comment %}
> > [!note]
> > {{annotation.comment}}
{% endif %}
{% else %}{% if annotation.comment %}
> [!note]
> {{annotation.comment}}
> [Page {{annotation.pageLabel}}]({{annotation.desktopURI}})
{% endif -%}{% endif -%}
{% if annotation.imageRelativePath %}
![[{{annotation.imageRelativePath}}]]
{% endif -%}
{% endif %}{% endfor %}

# Notes
{% persist "notes" %}
{% endpersist %}