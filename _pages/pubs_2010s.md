---
title: "Publications"
permalink: /pubs_2010s/
classes: wide
---

<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">
{% assign publications_by_year = site.publications | group_by_exp: "publication", "publication.date | date: '%Y'" | reverse %}

<h2> <a href="{{ '/publications/' | relative_url }}" >2020-Present </a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2010-2019 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="{{ '/pubs_2000s/' | relative_url }}" >2000-2009</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="{{ '/pubs_1990s/' | relative_url }}" >1990-1999</a>  </h2>

{% for year_group in publications_by_year %}
{% assign year = year_group.name | plus: 0 %}
{% if year >= 2010 and year <= 2019 %}
<h3> {{ year_group.name }} </h3>

{% for publication in year_group.items %}
<div class="three-col-table">
    <div class="three-col-table-left"> 
        <b>Title:</b><br><a href="{{ publication.url }}">{{ publication.title }}</a>
    </div>
    <div class="four-col-table-center1">
        <b>Authors:</b><br>{{publication.authors_string}}
    </div>
    <div class="four-col-table-center2">
        <b>Publication:</b><br>
        {% if publication.type == "journal_article" %}
        {{publication.journal}}
        {%elsif publication.type =="book_chapter"%}
        {{publication.book_title}}
        {%endif%}
    </div>
    <div class="four-col-table-right">
        <b>Data and Code:</b><br>
        {% if publication.data_loc != "" %}
        <a href="{{publication.data_loc}}">Data<br></a>
        {%endif%}
        {% if publication.code_loc != "" %}
        <a href="{{publication.code_loc}}">Code</a>
        {%endif%}
    </div>
</div>
    {% endfor %}
{%endif%}

{% endfor %}
