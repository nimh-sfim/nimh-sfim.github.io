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
<div class="content-list">
    <div class="publication-outer"> 
        <b>Title:</b><br><a href="{{ publication.url }}">{{ publication.title }}</a>
    </div>
    <div class="publication-authors">
        <b>Authors:</b><br>{{publication.authors_string}}
    </div>
    <div class="publication-outer">
        <b>Publication:</b><br>
        {% if publication.type == "journal_article" %}
        {{publication.journal}}
        {%elsif publication.type =="book_chapter"%}
        {{publication.book_title}}
        {%endif%}
    </div>
</div>

    {% endfor %}
{% endfor %}
