---
title: "Projects"
permalink: /projects/
classes: wide
---
<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

<h2> Active Projects </h2>

{% for project in site.projects %}
{% if project.status == "active" %}
<div class="project-list">
    <div class="project-item">
    <b>Title:</b><br>
    <a href="{{ project.url }}"> {{ project.title }} </a>
    </div>
    <div class="project-item">  
    <b>Summary:</b><br>
    {% assign first_sentence = project.summary | split: '.' | first %}
    {{ first_sentence | truncate: 100}}
    </div>
</div>
{% endif %}
{% endfor %}
