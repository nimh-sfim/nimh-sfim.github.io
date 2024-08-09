---
title: "Lab Members"
permalink: /members/
---

<div class="members-list">
  {% for member in site.members %}
    <div class="member-item">
      <a href="{{ member.url }}">
        <img src="{{ member.photo }}" alt="{{ member.name }}" class="member-photo">
        <h2>{{ member.name }}</h2>
        <h3>{{ member.position }}</h3>
      </a>
    </div>
  {% endfor %}
</div>
