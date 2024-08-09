---
title: "Lab Members"
permalink: /members/
classes: wide
---
<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

<h2> Current </h2>

{% for member in site.current_members %}
<div class="members-list">
    <div class="member-item">
      <a href="{{ member.url }}"> <img src="{{ member.photo }}" alt="{{ member.name }}" class="small-photo"> </a>
    </div>
    <div class="member-item">  
      <b>Name:</b><br>
      <a href="{{ member.url }}"> {{ member.name }}</a>
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

{% endfor %}

<h2> Former </h2>

{% for member in site.former_members %}
<div class="members-list">
    <div class="member-item">
      <img src="{{ member.photo }}" alt="{{ member.name }}" class="small-photo">
    </div>
    <div class="member-item">  
      <b>Name:</b><br>
      {{ member.name }}
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

{% endfor %}
