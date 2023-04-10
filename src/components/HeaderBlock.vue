<template>
  <header class="header">
    <div class="first-block">
      <h1 class="main-title">
      Дорогие Мама & Папа!<br>
      В нашей жизни есть счастливые и радостные моменты, которые хочется разделить с дорогими людьми. Ваша поддержка, понимание, любовь и дружба всегда были важны для нас. Поэтому мы приглашаем вас открыть вместе с нами новую страницу книги нашей жизни! Мы будем искренне рады разделить этот день вместе с вами.
      <span class="material-symbols-outlined">favorite</span>
      </h1>
    </div>
    <div class="menu"> 
      <ul class="menu-list">
        <li class="menu-item"><a class="menu-item__link" href="#dresscode">Дресс-код</a></li>
        <li class="menu-item"><a class="menu-item__link" href="#triumph">Церемония и торжество</a></li>
        <li class="menu-item"><a class="menu-item__link" href="#coordinator">Свадебный координатор</a></li>
        <li class="menu-item"><a class="menu-item__link" href="#photo">Фотографии с торжества</a></li>
      </ul>
    </div>
  </header>
</template>

<script setup lang="ts">

</script>

<style lang="scss">
.header {
  display: flex;
  flex-direction: column;

  .first-block {
    background-image: url("main.jpg");
    height: 500px;
    background-repeat: no-repeat, repeat;
    background-size: cover;
    vertical-align: middle;
    opacity: 0.8;
    font-family: 'Marck Script', cursive;
  }
  
  .main-title {
    padding-top: 10%;
    opacity: 1;
    width: 70%;
    padding-left: 15%;
    color: #ffe7e3;
    text-align: center;
  }

  .menu {
    margin: 0 auto;
  }

  .menu-list {
    display: flex;
    justify-content: space-between;
    column-gap: 40px;
    width: 100%;
    padding: 0;
    list-style: none;
  }

  .menu-item {
    font-size: 24px;
    padding: 10px 0;
    font-family: 'Marck Script', cursive;
    border-bottom: 1px solid #feb6b7;
    color: #855f5f;
    transition: color .3s, border .3s;
  }
  .menu-item:hover {
    color: #feb6b7;
  }
  .menu-item__link {
    text-decoration: none;
    color: inherit;
  }
}
</style>