---
title: Procedures
nav_order: 2
---

# Procedures

Various procedures and rules to follow.
{: .fs-6 .fw-300 }

{% assign section_pages = site.pages | where_exp: "p", "p.path contains 'docs/procedures/' and p.name != 'index.md'" | sort: "title" %}
<ul>
{% for p in section_pages %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>