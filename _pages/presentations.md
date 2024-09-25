---
title: "Presentations"
permalink: /presentations/
classes: wide
---

<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

{% for presentation in site.presentations %}
<div class="content-list">
    <div class="presentation-item">
        <b>Title: </b><br><a href="{{presentation.url}}">{{presentation.title}}</a><br>
    </div>
    <div class="presentation-item">
        {% if presentation.date%}
        {%assign pres_date = presentation.date % }
        {%else%}
        {%assign pres_date = ""%}
        {%endif%}
        <b>Presented on: </b><br>{{pres_date}} <br>
    </div>
    <div class="presentation-item">
        {% assign conference_item = site.conferences | where: "conference_id", presentation.conference_id | first %}
        <b>Conference: </b><br><a href="{{conference_item.url}}">{{conference_item.title}}</a> <br>
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
