---
title: "Former Lab Members"
permalink: /former-lab-members/
classes: wide
---
<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

<h2> <a href="{{ '/members/' | relative_url }}" >Current</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Former </h2>

{% assign former_staff_by_year = site.members | group_by_exp: "member", "member.end_date | date: '%Y'" | reverse %}

{% for year_group in former_staff_by_year %}

{% if year_group.name%}

<h2> {{ year_group.name }} </h2>

{% for member in year_group.items %}
{% if member.status == "former" %}
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
</div>
{% endif %}
{%endfor%}
{%endif%}

{% endfor %}
