<template>
  <div class="place" id="triumph">
    <div>
      <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2361.960958236422!2d87.01881379999999!3d53.70114159999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x42d0be2a6a3a5dc1%3A0x429cdaa438c4c6b!2z0JvQuNGB0YLQstGP0L3RgdC60L7QtSDRiC4sIDE3LCDQndC-0LLQvtC60YPQt9C90LXRhtC6LCDQmtC10LzQtdGA0L7QstGB0LrQsNGPINC-0LHQuy4sINCg0L7RgdGB0LjRjywgNjU0MDI4!5e0!3m2!1sru!2sge!4v1681045730025!5m2!1sru!2sge" width="600" height="450" style="border:0;" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
    <div class="placeinformation" >
      <p>
        Сбор гостей в 14:50 по адресу Листвянское ш., 17, Новокузнецк, Кемеровская обл. (Шатер)<br>
        Если вам нужен трансфер до места торжества и обратно, сообщите нам об этом.
      </p>
      <form class="place-form">
        <input id="transfer-there" type="radio" name="transfer" value="there" class="form-input">
        <label for="transfer-there" class="form-label">Трансфер только туда</label>
        <input id="transfer-there-back" type="radio" name="transfer" value="there-back" class="form-input">
        <label for="transfer-there-back" class="form-label">Трансфер туда и обратно</label>
        <input id="transfer-back" type="radio" name="transfer" value="back" class="form-input">
        <label for="transfer-back" class="form-label">Трансфер только обратно</label>
        <input id="transfer-no" type="radio" name="transfer" value="no" class="form-input">
        <label for="transfer-no" class="form-label">Трансфер не нужен</label>
        <button type="submit" class="send-form">Отправить ответ</button>
      </form>
    </div>
  </div>
</template>

<style scoped lang="scss">
.place {
  display: flex;
}
.placeinformation {
  margin: 20px;
  font-size: 24px;
  color: #855f5f;
}
.place-form {
  margin-top: 10px;
  color: #855f5f;
  font-size: 20px;
}
</style>