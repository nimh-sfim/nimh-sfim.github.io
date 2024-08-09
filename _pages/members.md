---
title: "Lab Members"
permalink: /members/
---
{% for member in site.members %}
<div class="members-list">
    <div class="member-item">
      <a href="{{ member.url }}"> <img src="{{ member.photo }}" alt="{{ member.name }}"> </a>
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
