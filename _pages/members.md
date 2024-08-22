---
title: "Lab Members"
permalink: /members/
classes: wide
---
<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

<h2> Current &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="{{ '/former-lab-members/' | relative_url }}" >Former</a> </h2>

{% assign sorted_members = site.members | sort: 'weight' %}
{% for member in sorted_members %}
{% if member.status == "current" %}
<div class="content-list">
    <div class="member-list-photo">
      <a href="{{ member.url }}"> <img src="{{ member.photo }}" alt="{{ member.title }}" class="small-photo"> </a>
    </div>
    <div class="member-item">  
      <b>Name:</b><br>
      <a href="{{ member.url }}"> {{ member.title }}</a>
    </div>
    <div class="member-item"> 
    <b>Position:</b><br>
      {{ member.position }}
    </div>
    <div class="member-item">
    <b>Email:</b><br>
     {{member.email}}
     </div>
     <div class="member-item">
     <b>Phone:</b><br>
      {{member.phone}}
    </div>
</div>
{% endif %}
{% endfor %}
