<template>
  <div class="guest-page">
    <HeaderBlock />
    <div class="content">
      <ConfirmationBlock />
      <DresscodeBlock />
      <PlaceBlock />
      <CoordinatorBlock />
      <PhotoBlock />
    </div>
    <button @click="topFunction" id="up" title="Go to top" :class="['up-button', {_hidden: upIsHidden}]">
      <span class="material-symbols-outlined up-button-icon">expand_less</span>
    </button>
    <div :class="['modal', {_open: isShowModal}]">
      <p class="modal-text">Форма успешно отправлена!</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import { useStore } from '@/store/index'
import HeaderBlock from '@/components/HeaderBlock.vue';
import ConfirmationBlock from '@/components/ConfirmationBlock.vue';
import DresscodeBlock from '@/components/DresscodeBlock.vue';
import PlaceBlock from '@/components/PlaceBlock.vue';
import CoordinatorBlock from '@/components/CoordinatorBlock.vue';
import PhotoBlock from '@/components/PhotoBlock.vue';
import { computed, onMounted, ref } from 'vue';

const store = useStore();
const { isShowModal } = storeToRefs(store);

const topFunction = () => {
  window.scrollTo({
    top: 0,
  })
}

const topHeight = ref(document.documentElement.scrollTop);
const upIsHidden = computed(() => {
  return topHeight.value < 200;
})

onMounted(() => {
  window.addEventListener('scroll', () => {
    topHeight.value = document.documentElement.scrollTop
  })
})
</script>

<style lang="scss" scoped>
.content {
  width: 70%;
  margin: 50px auto;  
  color: #855f5f;
  @media (max-width: 1150px) {
    width: 80%;
  }

  @media (max-width: 415px) {
    width: 90%;
  }

  @media (max-width: 950px) {
    margin: 30px auto;
  }
}
.up-button {
  position: fixed;
  bottom: 20px;
  right: 100px;
  z-index: 99;
  background-color: rgba(0, 0, 0, 0);
  border-radius: 50%;
  border: none;
  outline: none;
  color: #feb6b7;
  cursor: pointer;
  transition: color .3s, background-color .3s;

  &._hidden {
    display: none;
  }

  &:hover {
    background-color: #ffe7e3;
    color: #855f5f;
  }

  @media (max-width: 900px) {
    right: 50px;
  }
}
.up-button-icon {
  font-size: 50px;
}
.modal {
  position: fixed;
  top: -100px;
  right: 20px;
  width: 150px;
  height: 40px;
  padding: 10px 20px;
  border: 2px solid #855f5f;
  font-size: 18px;
  transition: top .4s;

  &._open {
    top: 20px;
  }
}
</style>
