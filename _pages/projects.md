---
title: "Projects"
permalink: /projects/
classes: wide
---
<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

<h2> Active Projects </h2>

{% for project in site.projects %}
{% if project.status == "current" %}
<div class="project-list">
    <div class="project-item">
    <b>Title:</b><br>
    <a href="{{ project.url }}"> {{ project.name }} </a>
    </div>
    <div class="project-item">  
        <b>Summary:</b><br>
        {{ project.email}}
    </div>
</div>
{% endif %}
{% endfor %}
