---
layout: home
---

Hi, this is my space for Heat Pump selection and analysis while I make progress to go low-carbon in my 1930s detatched house 
in the south of England, UK.

This is very much an ad-hoc selection of notes so far but you may find some of it useful...


<h1>Latest Post</h1>

{% assign post = site.posts.first %}
<h3><a class="post-link" href="{{ post.url }}">{{ post.title }}</a></h3>
<span class="post-meta">{{ post.date | date: "%d %B %Y" }}</span>
<div>{{ post.content  }}</div>

<h1>Recent Posts</h1>
{% for post in site.posts offset:1 limit:5 %}
... Show the next two posts ...
{% endfor %}