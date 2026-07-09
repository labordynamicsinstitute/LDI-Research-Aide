---
title: Email templates
nav_order: 3
---

# Email templates

Various templates related to email communication are listed below. If further instructions exist, they will be linked.
{: .fs-6 .fw-300 }

{% assign section_pages = site.pages | where_exp: "p", "p.path contains 'docs/emails/' and p.name != 'index.md'" | sort: "title" %}
<ul>
{% for p in section_pages %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>
