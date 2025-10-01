---
title: "Former Members"
permalink: /former-members/
classes: wide
---
<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

<h2> <a href="{{ '/people/' | relative_url }}" >Current</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Former </h2>
{% include shutdown_banner.html %}
{% assign sorted_members = site.members | sort: 'end_date' | reverse %}

{% assign current_year = "" %}

{% for member in sorted_members %}
{%if member.status == "former"%}
{% assign end_year = member.end_date %}

{% if end_year != current_year %}
<h2>{{ end_year }}</h2>
{% assign current_year = end_year %}
{% endif %}

<div class="content-list">
<div class="member-list-photo">
<a href="{{ member.url }}"> {%if member.photo%}  <img src="{{ member.photo  | relative_url }}" alt="{{ member.title }}" class="small-photo"> {%endif%} </a>
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
{%endfor%}
