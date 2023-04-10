<template>
  <div class="confirmation-block">
    <div>
      <span class="material-symbols-outlined notesicon">clinical_notes</span>
    </div>
    <div class="meetingconfirmation">
      <div class="m0 ">
        <span class="bold-text">Подтвердите присутсвие</span>
      </div>
      <div class="m0">
        <form class="confirmation-form">
          <div class="input-group">
            <input type="radio" name="field" class="confirmation-form__input">
            <label for="k1"></label>Присутсвие подверждаю<br>
            <input type="radio" name="field" class="confirmation-form__input">
            <label for="k2"></label>К сожалению, не смогу быть
          </div>
          <div class="input-group">
            <input type="radio" name="field2" class="confirmation-form__input">
            <label for="k4"></label>Буду один/одна<br>
            <input type="radio" name="field2" class="confirmation-form__input">
            <label for="k5"></label>Буду с парой
          </div>
          <div class="input-group">
            <input type="radio" name="field3" class="confirmation-form__input">
            <label for="k3"></label>Буду на машине
          </div>
        </form>
      </div>
      <div class="submit-wrapper">
        <button type="submit" class="save-form">Отправить</button>
      </div>
      <div class="m0">
        <p class="fz-24">Второй день торжества будет проходить за городом 17.06.2023 сбор в 14:00 (место будет озвучено в день свадьбы)</p>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.bold-text {
  font-size: 26px;
  font-weight: bold;
}
.fz-24 {
  font-size: 24px;
}
.m0 {
  margin: 0;
}
.confirmation-block {
  display: flex;
  flex-direction: row;
}
.notesicon {
  font-size: 120px; 
  margin-top: 80%;
}
.meetingconfirmation {
  display: flex;
  flex-direction: column;
  margin: 40px;
}
.confirmation-form {
  margin-top: 10px;
  font-family: 'Marck Script', cursive;
  color: #855f5f;
  font-size: 20px;
  width:100%;
  display: flex;
}
.input-group + .input-group {
  margin-left: 20px;
}  
.confirmation-form__input {
  display: none;
}
.confirmation-form__input + label {
  display: inline-block;
  vertical-align: top;
  width: 20px;
  height: 20px;
  border: 1px solid #855f5f;
  margin: 5px 10px 5px 0;
  border-radius: 10px;
}
.confirmation-form__input:checked + label {
  background: #855f5f;
}
.save-form{
  pointer-events: none;
  font-family: 'Marck Script', cursive;
  font-size: 20px;
  border: 1px solid #feb6b7;
  background-color: white;
  margin-top: 20px;
  color: #855f5f;
  padding: 5px 10px;
}
.save-form:hover {
  color: #feb6b7;
  font-size: 22px;
}
.confirmation-form__input:checked + label ~ .save-form {
  pointer-events: auto;
  color: #855f5fv;
}
.submit-wrapper {
  width:100%; 
  margin: 10px 0 20px;
}
</style>