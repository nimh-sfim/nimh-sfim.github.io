---
title: "Publications"
permalink: /publications/
classes: wide
---

<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

{% assign publications_by_year = site.publications | group_by_exp: "publication", "publication.date | date: '%Y'" | reverse %}

{% for year_group in publications_by_year %}
<h2> {{ year_group.name }} </h2>

{% for publication in year_group.items %}
<div class="presentation-list">
    <div> 
        <b>Title:</b><br><a href="{{ publication.url }}">{{ publication.title }}</a>
    </div>
        <b>Authors:</b><br>{{publications.authors_string}}
    <div>
    </div>
    <div>
        <b>Publication:</b><br>
        {{publication.journal}}
    </div>
</div>

    {% endfor %}
{% endfor %}
