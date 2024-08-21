---
title: "Projects"
permalink: /projects/
classes: wide
---
<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

<h2> Active Projects </h2>

{% for project in site.projects %}
{% if project.status == "current" %}
<div class="content-list">
    <div class="project-title">
    <b>Title:</b><br>
    <a href="{{ project.url }}"> {{ project.title }} </a>
    </div>
    <div class="project-summary">  
        <b>Summary:</b><br>
        {{ project.short_summary}}
    </div>
</div>
{% endif %}
{% endfor %}
