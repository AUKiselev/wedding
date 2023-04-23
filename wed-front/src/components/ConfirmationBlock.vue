<template>
  <div class="confirmation-block">
    <div class="icon-wrapper">
      <span class="material-symbols-outlined notesicon">clinical_notes</span>
    </div>
    <div class="meeting-confirmation">
      <span class="bold-text">Подтвердите присутсвие</span>
      <form v-bind="userForm" class="confirmation-form">
        <div class="input-group">
          <input
            id="presence-yes"
            type="radio"
            v-model="userForm.will_come"
            :value="true"
            class="confirmation-form__input form-input"
          >
          <label for="presence-yes" class="confirmation-form__label form-label">Присутсвие подверждаю</label>
          <input
            id="presence-no"
            type="radio"
            v-model="userForm.will_come"
            :value="false"
            class="confirmation-form__input form-input"
          >
          <label for="presence-no" class="confirmation-form__label form-label">К сожалению, не смогу быть</label>
        </div>
        <div class="input-group">
          <input
            id="is-alone-yes"
            type="radio"
            v-model="userForm.solo"
            :value="true"
            class="confirmation-form__input form-input"
          >
          <label for="is-alone-yes" class="confirmation-form__label form-label">Буду один/одна</label>
          <input
            id="is-alone-no"
            type="radio"
            v-model="userForm.solo"
            :value="false"
            class="confirmation-form__input form-input"
          >
          <label for="is-alone-no" class="confirmation-form__label form-label">Буду с парой</label>
        </div>
        <div class="input-group">
          <input
            id="on-car-yes"
            type="checkbox"
            name="on-car"
            v-model="userForm.have_car"
            class="confirmation-form__input form-input"
          >
          <label for="on-car-yes" class="confirmation-form__label form-label">Буду на машине</label>
        </div>
      </form>
      <p class="fz-24 descripdion">Пожалуйста, заполните поля. В блоке с картой будет кнопка отправки формы.</p>
      <p class="fz-24">Второй день торжества будет проходить за городом 17.06.2023 сбор в 14:00 (место будет озвучено в день свадьбы)</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useRoute } from "vue-router";
import { storeToRefs } from 'pinia';
import { useStore } from '@/store/index'

const route = useRoute();
const user = route.params.user as string;

const store = useStore();
const { userForm } = storeToRefs(store);

onMounted(() => {
  userForm.value.slug = user;
})
</script>

<style scoped lang="scss">
.bold-text {
  font-size: 26px;
  font-weight: bold;
}
.fz-24 {
  font-size: 24px;

  @media (max-width: 768px) {
    font-size: 18px;
  }
}
.confirmation-block {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.notesicon {
  font-size: 120px; 
}
.meeting-confirmation {
  display: flex;
  flex-direction: column;
  margin: 40px;
  margin-right: 0;

  @media (max-width: 950px) {
    margin: 0 0 20px 0;
  }
}
.confirmation-form {
  margin-top: 10px;
  color: #855f5f;
  font-size: 20px;
  width:100%;
  display: flex;

  @media (max-width: 768px) {
    font-size: 16px;
  }

  @media (max-width: 415px) {
    font-size: 14px;
  }
}
.input-group + .input-group {
  margin-left: 20px;

  @media (max-width: 550px) {
    margin-left: 15px;
  }
}
.submit-wrapper {
  width:100%; 
  margin: 10px 0 20px;
}

.descripdion {
  margin: 20px 0
}
</style>