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
<b>Presented on: </b>{{presentation.date}} <br>
{% assign conference = site.data.conferences[presentation.conference] %}
<b>Project: </b><a href="{{conference.url}}">{{conference.title}}</a> <br>
<b> Summary: </b><br>
<b>Presenters: </b><br>
<ul>
{% for presenter_id in presentation.presenters %}
      {% assign presenter = site.data.members[presenter_id] %}
      <li>
        <a href="{{presenter.url}}">{{ presenter.name }}</a>
      </li>
{% endfor %}
</ul>
<b>Download: </b>
</div>
</div>
{% endfor %}
