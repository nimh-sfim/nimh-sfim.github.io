---
title: "Conferences"
permalink: /conferences/
classes: wide
---

<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

{% assign sorted_conferences = site.conferences | sort: 'date' | reverse %}
{% for conference in sorted_conferences %}
<div class="content-list">
    <div class="project-item">
    <b>Name:</b><br>
    <a href="{{ conference.url }}"> {{ conference.name }} </a>
    </div>
    <div class="project-item">  
        <b>Location:</b><br>
        {{ conference.location }}
    </div>
</div>
{% endfor %}
