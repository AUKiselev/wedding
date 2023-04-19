<template>
  <div class="place" id="triumph">
    <div class="map-wrapper">
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2361.960958236422!2d87.01881379999999!3d53.70114159999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x42d0be2a6a3a5dc1%3A0x429cdaa438c4c6b!2z0JvQuNGB0YLQstGP0L3RgdC60L7QtSDRiC4sIDE3LCDQndC-0LLQvtC60YPQt9C90LXRhtC6LCDQmtC10LzQtdGA0L7QstGB0LrQsNGPINC-0LHQuy4sINCg0L7RgdGB0LjRjywgNjU0MDI4!5e0!3m2!1sru!2sge!4v1681045730025!5m2!1sru!2sge"
        width="100%"
        height="450"
        style="border:0;"
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
      ></iframe>
    </div>
    <div class="place-information" >
      <p>
        Сбор гостей в 14:50 по адресу Листвянское ш., 17, Новокузнецк, Кемеровская обл. (Шатер)<br>
        Если вам нужен трансфер до места торжества и обратно, сообщите нам об этом.
      </p>
      <form class="place-form" v-bind="transferForm">
        <input id="transfer-there-back" type="radio" name="transfer" v-model="transferForm.transfer" value="there-back" class="form-input">
        <label for="transfer-there-back" class="form-label">Трансфер туда и обратно</label>
        <input id="transfer-there" type="radio" name="transfer" v-model="transferForm.transfer" value="there" class="form-input">
        <label for="transfer-there" class="form-label">Трансфер только туда</label>
        <input id="transfer-back" type="radio" name="transfer" v-model="transferForm.transfer" value="back" class="form-input">
        <label for="transfer-back" class="form-label">Трансфер только обратно</label>
        <input id="transfer-no" type="radio" name="transfer" v-model="transferForm.transfer" value="no" class="form-input">
        <label for="transfer-no" class="form-label">Трансфер не нужен</label>
        <button type="submit" class="send-form" :disabled="submitDisabled">Отправить ответ</button>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive } from 'vue';

const transferForm = reactive({
  transfer: 'there-back'
})

const submitDisabled = computed(() => {
  return transferForm.transfer === null
})
</script>

<style scoped lang="scss">
.map-wrapper {
  width: 100%;
}
.place {
  display: flex;
  column-gap: 20px;

  @media (max-width: 900px) {
    flex-direction: column;
    row-gap: 30px;
  }
}
.place-information {
  max-width: 300px;
  font-size: 24px;
  color: #855f5f;

  @media (max-width: 900px) {
    max-width: none;
  }

  @media (max-width: 768px) {
    font-size: 18px;
  }
}
.place-form {
  margin-top: 10px;
  color: #855f5f;
  font-size: 20px;
}
</style>