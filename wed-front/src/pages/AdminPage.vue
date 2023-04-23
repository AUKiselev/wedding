<template>
  <div class="admin-page">
    <div v-if="!isAuth" class="auth-form">
      <div class="input-block">
        <span class="label">Логин</span>
        <input v-model="login" @change="inputCheck" type="text" class="input">
      </div>
      <div class="input-block">
        <span class="label">Пароль</span>
        <input v-model="pass" @change="inputCheck" type="password" class="input">
      </div>
    </div>
    <div v-else class="results">
      <div class="row" v-for="(guest, index) of guests" :key="`guest-list-${index}`">
        <p class="name">{{ getName(guest) }}</p>
        <p class="presence">{{ willCome(guest) }}</p>
        <p class="is-alone">{{ isAlone(guest) }}</p>
        <p class="on-car">{{ onCar(guest) }}</p>
        <p class="transfer">{{ transfer(guest) }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import api from '@/api'
import guestList from '@/mock/guestList.json'

const isAuth = ref(false);
const login = ref('');
const pass = ref('');

const inputCheck = () => {
  if (login.value === 'Danil' && pass.value === 'Mila') {
    isAuth.value = true;
  }
}

const guests = ref([])

const getName = (guest) => {
  if (!guest || !guest.slug) return;
  if (guest.slug === 'alexander_m') return guestList[guest.slug].slice(7) + ' Москаленко';
  let name;
  if (guestList[guest.slug]) {
    name = guestList[guest.slug].slice(7);
  }
  return name;
}

const willCome = (guest) => {
  if (guest.will_come) {
    return 'Буду присутствовать';
  }
  return 'Присутствовать не смогу';
}

const isAlone = (guest) => {
  if (guest.solo) {
    return 'Буду один(одна)';
  }
  return 'Буду с парой';
}

const onCar = (guest) => {
  if (guest.have_car) {
    return 'Буду на машине';
  }
  return 'Буду без машины';
}

const transfer = (guest) => {
  if (guest.transfer_to && guest.transfer_from) return 'Трансфер туда и обратно'
  else if (guest.transfer_to) return 'Трансфер только туда'
  else if (guest.transfer_from) return 'Трансфер только обратно'
  return 'Трансфер не нужен'
}

onMounted(async () => {
  const response = await api.get('/claims/');

  guests.value = response;
})
</script>

<style scoped lang="scss">
.admin-page {
  width: 90%;
  margin: 0 auto;

  .auth-form {
    max-width: 300px;
    margin: 20% auto 0;
    padding: 20px;
    border-radius: 4px;
    border: 2px solid #855f5f;
    font-size: 20px;
    color: #855f5f;
  }

  .input-block {
    display: flex;
    flex-direction: column;
    row-gap: 5px;

    & + .input-block {
      margin-top: 20px;
    }

    .input {
      height: 20px;
      border-radius: 4px;
      outline:none;

      &:focus-visible {
        outline: 1px solid #855f5f;
      }
    }
  }

  .results {
    display: flex;
    flex-direction: column;
    row-gap: 15px;
    margin-top: 30px;

    .row {
      display: flex;
      justify-content: space-between;
      width: 100%;
      column-gap: 20px;
      border-bottom: 1px solid black;

      p {
        width: 20%;
        font-size: 20px;

        @media (max-width: 768px) {
          font-size: 18px;
        }
        @media (max-width: 650px) {
          font-size: 16px;
        }
        @media (max-width: 540px) {
          font-size: 14px;
        }
        @media (max-width: 490px) {
          font-size: 12px;
        }
        @media (max-width: 390px) {
          font-size: 10px;
        }
      }
    }
  }
}
</style>