---
title: "Lab Members"
permalink: /members/
classes: wide
---
<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

<h2> Current </h2>

{% assign sorted_members = site.members | sort: 'weight' %}
{% for member in sorted_members %}
{% if member.status == "current" %}
<div class="content-list">
    <div class="member-item">
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

<h2> Former </h2>

{% for member in site.members %}
{% if member.status == "former" %}
<div class="content-list">
    <div class="member-item">
      <img src="{{ member.photo }}" alt="{{ member.title }}" class="small-photo">
    </div>
    <div class="member-item">  
      <b>Name:</b><br>
      {{ member.title }}
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
