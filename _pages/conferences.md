---
title: "Conferences"
permalink: /conferences/
classes: wide
---

<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">
{% assign sorted_conferences = site.conferences | sort: 'date' | reverse %}
{% for conference in sorted_conferences %}
<div class="content-list">
    <div class="conference-name">
    <b>Name:</b><br>
    <a href="{{ conference.url }}"> {{ conference.title }} </a>
    </div>
    <div class="conference-location">  
        <b>Location:</b><br>
        {{ conference.location }}
    </div>
</div>
{% endfor %}
