<template>
  <div id="coordinator" class="coordinator">
    <p>
      Свадебный координатор – Екатерина<br>
      Тел.: <a href="tel:89234739377" class="phone">+7(923)-473-93-77</a><br>
      Екатерина с радостью ответит на все вопросы, связанные с торжеством. Если вы подготовили для нас сюрприз или творческий подарок, не забудьте предупредить её. Екатерина поможет воплотить вашу идею или отговорит вас <span class="material-symbols-outlined">sentiment_satisfied</span><br>
      <span class="warning">Если у&nbsp;вас есть аллергия или вы&nbsp;не&nbsp;едите мясо(свинину) или рыбу, сообщите об&nbsp;этом заранее нам или Екатерине!</span>
      Так же приветствуются записанные заранее на камеру поздравления.<br>Отправить Екатерине максимум за неделю до даты торжества.
    </p>
  </div>
</template>

<style scoped lang="scss">
.coordinator {
  color: #855f5f;
  font-size: 24px;
  text-align: center;
  margin: 40px auto;

  @media (max-width: 768px) {
    margin-top: 20px;
    margin-bottom: 20px;
    font-size: 18px;
  }
}
.phone {
  text-decoration: none;
  color:#feb6b7;

  &:hover {
    text-decoration: underline;
  }
}

.warning {
  display: block;
  color: #ff6a5d;
}
</style>