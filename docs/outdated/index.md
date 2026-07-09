---
title: Probably outdated pages
---

# Probably outdated pages

These pages are likely outdated and should be reviewed for accuracy. 
{: .fs-6 .fw-300 }

{% assign section_pages = site.pages | where_exp: "p", "p.path contains 'docs/outdated/' and p.name != 'index.md'" | sort: "title" %}
<ul>
{% for p in section_pages %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>