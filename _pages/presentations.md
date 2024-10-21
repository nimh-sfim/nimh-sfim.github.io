---
title: "Presentations"
permalink: /presentations/
classes: wide
---

<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

{% assign presentations_by_year = site.presentations | group_by_exp: "presentation", "presentation.date | date: '%Y'" | reverse %}

<h2> 2020-Present &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="{{ '/pres_2010s/' | relative_url }}" >2010-2019</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="{{ '/pres_2000s/' | relative_url }}" >2000-2009</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="{{ '/pres_1990s/' | relative_url }}" >1990-1999</a>  </h2>

{% for year_group in presentations_by_year %}

{% assign year = year_group.name | plus: 0 %}
{% if year >= 2020 %}
<h3> {{ year_group.name }} </h3>

{% for presentation in year_group.items %}
<div class="content-list">
    <div class="presentation-item">
        <b>Title: </b><br><a href="{{presentation.url}}">{{presentation.title}}</a><br>
    </div>
    <div class="presentation-item">
        <b>Presented on: </b><br>{{presentation.date | date: "%B %Y"}} <br>
    </div>
    <div class="presentation-item">
        {% assign conference_item = site.conferences | where: "conference_id", presentation.conference_id | first %}
        <b>Conference/Event: </b><br><a href="{{conference_item.url}}">{{conference_item.title}}</a> <br>
    </div>
    <div class="presentation-item">
        <b>Project: </b><br>
        {% if presentation.project_id%}
        {% assign project = site.projects | where: "project_id", presentation.project_id | first %}
        <a href="{{project.url}}">{{project.title}}</a><br>
        {%endif%}
    </div>
    <div class="presentation-item">
        <b>Presenters: </b><br>
            <ul>
            {% for presenter_id in presentation.presenters %}
                {% assign presenter = site.members | where: "presenter_id", presenter_id | first %}
                <li>
                    <a href="{{presenter.url}}">{{ presenter.title }}</a>
                </li>
            {% endfor %}
            </ul>
    </div>
</div>
{% endfor %}
{%endif%}
{%endfor%}
