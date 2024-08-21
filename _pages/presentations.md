---
title: "Presentations"
permalink: /presentations/
classes: wide
---

<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

{% for presentation in site.presentations %}
<div class="content-list">
    <div class="presenation-item">
        <b>Title: </b><a href="{{presentation.url}}">{{presentation.title}}</a><br>
        <b>Presented on: </b>{{presentation.date | date: "%B %Y"}} <br>
        {% assign conference_item = site.conferences | where: "conference_id", presentation.conference_id | first %}
        <b>Conference: </b><a href="{{conference_item.url}}">{{conference_item.name}}</a> <br>
        <b>Project: </b>
        {% assign project = site.projects | where: "project_id", presentation.project_id | first %}
        <a href="{{project.url}}">{{project.title}}</a><br>
        <b>Summary: </b><br>
        <b>Presenters: </b><br>
            <ul>
            {% for presenter_id in presentation.presenters %}
                {% assign presenter = site.members | where: "presenter_id", presenter_id | first %}
                <li>
                    <a href="{{presenter.url}}">{{ presenter.title }}</a>
                </li>
            {% endfor %}
            </ul>
        <b>Download: </b><a href="{{presentation.file}}">{{presentation.file_name}}</a>
    </div>
</div>
{% endfor %}
