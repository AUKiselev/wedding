<template>
  <header class="header">
    <div class="first-block">
      <h1 class="main-title">
        {{ guestName }}!<br>
        В нашей жизни есть счастливые и радостные моменты, которые хочется разделить с дорогими людьми. Ваша поддержка, понимание, любовь и дружба всегда были важны для нас. Поэтому мы приглашаем вас открыть вместе с нами новую страницу книги нашей жизни! Мы будем искренне рады разделить этот день вместе с вами.
        <span class="material-symbols-outlined">favorite</span>
        <span class="wedding-date">16.06.2023 г. в 15:00</span>
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
import { onMounted, ref } from 'vue';
import { useRoute } from "vue-router";
import guestList from '@/mock/guestList.json';

const guestName = ref<string | null>(null)
const route = useRoute();

onMounted(() => {
  const user = route.params.user as string;
  // @ts-ignore
  guestName.value = guestList[user];
})
</script>

<style lang="scss">
.header {
  display: flex;
  flex-direction: column;

  .first-block {
    background-image: url("@/assets/img/main.jpg");
    height: 500px;
    background-repeat: no-repeat;
    background-size: cover;
    vertical-align: middle;
    opacity: 0.8;

    @media (max-width: 1000px) {
      height: 400px;
    }

    @media (max-width: 768px) {
      height: 350px;
    }

    @media (max-width: 650px) {
      height: 325px;
    }
  }
  
  .main-title {
    margin: 10% auto 0;
    width: 70%;
    opacity: 1;
    text-align: center;
    color: #ece4e2;

    @media (max-width: 1000px) {
      margin-top: 5%;
      width: 80%;
      font-size: 28px;
    }

    @media (max-width: 768px) {
      margin-top: 20px;
      font-size: 24px;
    }

    @media (max-width: 650px) {
      font-size: 22px;
    }

    @media (max-width: 550px) {
      font-size: 20px;
    }

    @media (max-width: 450px) {
      font-size: 18px;
    }

    @media (max-width: 360px) {
      font-size: 17px;
    }
  }

  .wedding-date {
    display: block;
    color: white;
  }

  .menu {
    margin: 0 auto;

    @media (max-width: 768px) {
      display: none;
    }
  }

  .menu-list {
    display: flex;
    justify-content: space-between;
    width: 100%;
    padding: 0;
    list-style: none;
  }

  .menu-item {
    font-size: 24px;
    padding: 10px 0;
    border-bottom: 1px solid #feb6b7;
    color: #855f5f;
    transition: color .3s, border .3s;

    @media (max-width: 1000px) {
      font-size: 20px;
    }

    @media (max-width: 800px) {
      font-size: 18px;
    }

    &:hover {
      color: #feb6b7;
    }

    & + .menu-item {
      margin-left: 40px;

      @media (max-width: 1000px) {
        margin-left: 20px;
      }
    }
  }
  .menu-item__link {
    text-decoration: none;
    color: inherit;
  }
}
</style>