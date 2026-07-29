---
layout: default
title: The Fracture Novels
---
<style>
.home-hero{padding:3rem 1.5rem 1.5rem;text-align:center;max-width:700px;margin:0 auto}
.home-hero .series-label{font-family:sans-serif;font-size:0.75rem;letter-spacing:0.15em;
  text-transform:uppercase;color:var(--muted);margin-bottom:0.5rem}
.home-hero h1{font-size:2.2rem;color:var(--accent);margin-bottom:0.4rem;line-height:1.2}
.home-hero .tagline{color:var(--muted);font-style:italic;font-size:0.95rem;margin-bottom:0.6rem}
.home-hero .author-line{font-size:0.85rem;color:var(--muted);margin-bottom:3rem}
.books-grid{display:flex;gap:3rem;flex-wrap:wrap;justify-content:center;
  max-width:700px;margin:0 auto;padding:0 1.5rem 3rem}
.book-card{flex:1;min-width:220px;max-width:270px;text-align:center}
.book-card img{width:210px;height:300px;object-fit:cover;
  box-shadow:0 6px 24px rgba(0,0,0,0.2);border-radius:3px;
  display:block;margin:0 auto 1.2rem}
.book-card .book-num{font-family:sans-serif;font-size:0.7rem;letter-spacing:0.12em;
  text-transform:uppercase;color:var(--muted);margin-bottom:0.3rem}
.book-card h2{font-size:1.05rem;margin-bottom:0.3rem;color:var(--text);line-height:1.3}
.book-card .book-subtitle{font-size:0.82rem;color:var(--muted);font-style:italic;margin-bottom:0.9rem}
.btn-read{display:inline-block;padding:0.5rem 1.2rem;background:var(--accent);
  color:#fff;border-radius:3px;font-size:0.82rem;font-family:sans-serif;
  text-decoration:none}
.btn-read:hover{opacity:0.88;text-decoration:none}
@media(max-width:480px){.books-grid{flex-direction:column;align-items:center}}
</style>
<div class="home-hero">
  <p class="series-label">The Fracture Novels</p>
  <h1>History does not repeat loudly.<br>It repeats precisely.</h1>
  <p class="tagline">Two dates. Two assassinations. One fracture.</p>
  <p class="author-line">Historical fiction by Arul &mdash; free to read</p>
</div>
<div class="books-grid">
  <div class="book-card">
    <img src="{{ site.baseurl }}/31-10-84/cover.png" alt="31.10.84 cover">
    <p class="book-num">Book I</p>
    <h2>31.10.84</h2>
    <p class="book-subtitle">A Nation on the Edge</p>
    <a href="{{ site.baseurl }}/31-10-84/" class="btn-read">Start Reading</a>
  </div>
  <div class="book-card">
    <img src="{{ site.baseurl }}/21-05-91/cover.png" alt="21.05.91 cover">
    <p class="book-num">Book II</p>
    <h2>21.05.91</h2>
    <p class="book-subtitle">Shadows of History</p>
    <a href="{{ site.baseurl }}/21-05-91/" class="btn-read">Start Reading</a>
  </div>
</div>
