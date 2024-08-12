---
title: "Presentations"
permalink: /presentations/
classes: wide
---

<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

{% for presentation in site.presentations %}
<div class="presentation-list">
<div class="presenation-item">
<b>Title: </b>{{presentation.title}}<br>
<b>Presented on: </b>{{presentation.date | date: "%B %Y"}} <br>
{% assign conference_item = site.conferences[presentation.conference] %}
<b>Conference: </b><a href="{{conference_item.url}}">{{conference_item.name}}</a> <br>
<b>Summary: </b><br>
<b>Presenters: </b><br>
<ul>
{% for presenter_id in presentation.presenters %}
    {% assign presenter = site.members | where: "id", presenter_id | first %}
      <li>
        <a href="{{presenter.url}}">{{ presenter.name }}</a>
      </li>
{% endfor %}
</ul>
<b>Download: </b>
</div>
</div>
{% endfor %}
