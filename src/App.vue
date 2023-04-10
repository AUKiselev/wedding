<template>
  <div class="page-wrapper">
    <HeaderBlock />
    <div class="content">
      <ConfirmationBlock />
      <div id="dresscode">
        <div>
          <span class="material-symbols-outlined" style="font-size: 120px;">styler</span>
        </div>
        <div style="font-size: 24px;">
          Мы очень ждем и с удовольствием готовимся к нашему незабываемому дню! Поддержите нас вашими улыбками и объятиями, а также красивыми нарядами в палитре торжества.<br>
          (Соблюдение дресс-кода обязательно)<br>
          Захватите с собой удобную обувь для танцев!<br>
          <span class="material-symbols-outlined">favorite</span>
        </div>
      </div>
      <div class="place" id="triumph">
        <div>
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2361.960958236422!2d87.01881379999999!3d53.70114159999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x42d0be2a6a3a5dc1%3A0x429cdaa438c4c6b!2z0JvQuNGB0YLQstGP0L3RgdC60L7QtSDRiC4sIDE3LCDQndC-0LLQvtC60YPQt9C90LXRhtC6LCDQmtC10LzQtdGA0L7QstGB0LrQsNGPINC-0LHQuy4sINCg0L7RgdGB0LjRjywgNjU0MDI4!5e0!3m2!1sru!2sge!4v1681045730025!5m2!1sru!2sge" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
        <div style="margin:20px;">
          <p>
            Сбор гостей в 14:50 по адресу Листвянское ш., 17, Новокузнецк, Кемеровская обл. (Шатер)<br>
            Если вам нужен трансфер до места торжества и обратно, сообщите нам об этом.
          </p>
          <form>
            <input type="radio" name="field4" id="mc1">
            <label for="mc1"></label>Трансфер только туда<br>
            <input type="radio" name="field4" id="mc2">
            <label for="mc2"></label>Трансфер туда и обратно<br>
            <input type="radio" name="field4" id="mc3">
            <label for="mc3"></label>Трансфер только обратно<br>
            <input type="radio" name="field4" id="mc4">
            <label for="mc4"></label>Трансфер не нужен<br>
            <button id="saveForm2" type="submit">Отправить ответ</button>
          </form>
        </div>
      </div>
      <div id="coordinator">
        <p>
          Свадебный координатор – Екатерина<br>
          Тел.: <a href="tel:89234739377" class="phone">+7(923)-473-93-77</a><br>
          Екатерина с радостью ответит на все вопросы, связанные с торжеством. Если вы подготовили для нас сюрприз или творческий подарок, не забудьте предупредить её. Екатерина поможет воплотить вашу идею или отговорит вас <span class="material-symbols-outlined">sentiment_satisfied</span><br>
          Так же приветствуются записанные заранее на камеру поздравления. Отправить Екатерине максимум за неделю до даты торжества.
        </p>
      </div>
      <div id="photo">
        <p>Скоро здесь появятся фотографии с торжества</p>
        <div class="loader"></div>
      </div>
    </div>
    <button @click="topFunction" id="up" title="Go to top"><span class="material-symbols-outlined" style="font-size: 50px;">expand_less</span></button>
  </div>
</template>

<script setup lang="ts">
import HeaderBlock from '@/components/HeaderBlock.vue';
import ConfirmationBlock from '@/components/ConfirmationBlock.vue';

const topFunction = () => {
  window.scrollTo({
    top: 0,
  })
}
</script>

<style lang="scss" scoped>
  
    .information,
    .meetingconfirmation {
      display: flex;
      flex-direction: column;
    }
    input {
      border: none;
      border-bottom: 2px solid #ffe7e3;
      width: 50%;
      height: 40px;
      margin: 10px 0 30px 0;
      outline:none;
      font-family: 'Marck Script', cursive;
      font-size: 20px;
    }
    .notesicon {
      font-size: 120px; 
      margin-top: 80%;
    }
    #dresscode div, 
    #confirmation div {
      margin: 20px;
    }
    #dresscode, 
    #confirmation {
      display: flex;
      flex-direction: row;
    }


    p {
      color: #855f5f;
      font-family: 'Marck Script', cursive;
    }
    .content {
      width: 70%;
      margin: 50px auto;
      font-family: 'Marck Script', cursive;
      color: #855f5f;
    }
    .place {
      width: 70%;
      margin: auto;
      display: flex;
    }
    form {
      margin-top: 10px;
      font-family: 'Marck Script', cursive;
      color: #855f5f;
      font-size: 20px;
    }    
    input[name=field],
    input[name=field2],
    input[name=field3],
    input[name=field4] {
      display: none;
    }
    input[name=field] + label,
    input[name=field2] + label,
    input[name=field3] + label,
    input[name=field4] + label {
      display: inline-block;
      vertical-align: top;
      width: 20px;
      height: 20px;
      border: 1px solid #855f5f;
      margin: 5px 10px 5px 0;
      border-radius: 10px;
    }
    input[name=field]:checked + label,
    input[name=field2]:checked + label,
    input[name=field3]:checked + label,
    input[name=field4]:checked + label {
      background: #855f5f;
    }
    #saveForm,
    #saveForm2 {
      pointer-events: none;
      font-family: 'Marck Script', cursive;
      font-size: 20px;
      border: 1px solid #feb6b7;
      background-color: white;
      margin-top: 20px;
      color: #855f5f;
      padding: 5px 10px;
    }
    #saveForm:hover, 
    #saveForm2:hover {
      color: #feb6b7;
      font-size: 22px;
    }
    input[name=field]:checked + label ~ #saveForm, 
    input[name=field2]:checked + label ~ #saveForm {
      pointer-events: auto;
      color: #855f5fv;
    }
    input[name=field4]:checked + label ~ #saveForm2 {
      pointer-events: auto;
      color: #855f5fv;
    }
    p {
      font-size: 24px;
    }
    .phone {
      text-decoration: none;
      color:#feb6b7;
    }
    .phone:hover {
      font-size: 25px;
    }
    .loader {
      border: 10px solid #f3f3f3;
      border-radius: 50%;
      border-top: 10px solid #feb6b7;
      width: 80px;
      height: 80px;
      -webkit-animation: spin 2s linear infinite; /* Safari */
      animation: spin 2s linear infinite;
      margin: 25px auto;
    }
    @-webkit-keyframes spin {
      0% { -webkit-transform: rotate(0deg); }
      100% { -webkit-transform: rotate(360deg); }
    }
    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    #up {
      display: none;
      position: fixed;
      bottom: 20px;
      right: 100px;
      z-index: 99;
      background-color: white;
      border: none;
      outline: none;
      color: #feb6b7;
      cursor: pointer;
    }
    #up:hover span {
      color: #555;
    }
</style>
