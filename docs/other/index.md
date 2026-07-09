---
title: Otherwise unclassified pages
nav_order: 10
---

# Otherwise unclassified pages

These pages don't neatly fit into the other categories. 
{: .fs-6 .fw-300 }

{% assign section_pages = site.pages | where_exp: "p", "p.path contains 'docs/other/' and p.name != 'index.md'" | sort: "title" %}
<ul>
{% for p in section_pages %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>