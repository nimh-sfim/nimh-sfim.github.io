---
title: "Former Lab Members"
permalink: /former-lab-members/
classes: wide
---
<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

<h2> <a href="{{ '/members/' | relative_url }}" >Current</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Former </h2>

{% assign sorted_members = site.members | sort: 'end_date' | reverse %}

{% assign current_year = "" %}

{% for member in sorted_members %}
  {%if member.status == "former"%}
  {% assign end_year = member.end_date | date: "%Y" %}

  {% if end_year != current_year %}
    <!-- Create a header for each year -->
    <h2>{{ end_year }}</h2>
    {% assign current_year = end_year %}
  {% endif %}

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

  {%endif%}
  {%endfor&}
  