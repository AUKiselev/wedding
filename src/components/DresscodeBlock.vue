<template>
  <div id="dresscode" class="dresscode">
  <div class="icon-wrapper">
    <span class="material-symbols-outlined dresscode-icon-span">styler</span>
  </div>
  <div class="dresscode-text">
    <p>
      Мы очень ждем и с удовольствием готовимся к нашему незабываемому дню! Поддержите нас вашими улыбками и объятиями, а также красивыми нарядами в палитре торжества:
    </p>
    <ul class="dresscode-colors">
      <li
        v-for="n in 7"
        :key="`dresscode-color-${n}`"
        :class="['dresscode-color', `color-${n}`]"
      >
      </li>
    </ul>
    <ul class="dresscode-colors">
      <li
        v-for="n in 7"
        :key="`dresscode-color-${n + 7}`"
        :class="['dresscode-color', `color-${n + 7}`]"
      >
      </li>
    </ul>
    <div class="dresscode-description">
      <span>(Соблюдение дресс-кода обязательно)</span>
      <span>Захватите с собой удобную обувь для танцев!</span>
      <span class="material-symbols-outlined">favorite</span>
    </div>
  </div>
</div>
</template>

<script setup lang="ts">
</script>

<style scoped lang="scss">
.dresscode {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.dresscode-icon{
  margin: 20px;
} 
.dresscode-icon-span {
  font-size: 120px;
}
.dresscode-text {
  margin: 40px;
  margin-right: 0;
  font-size: 24px;

  @media (max-width: 950px) {
    margin-top: 20px;
    margin-left: 0;
    font-size: 18px;
  }
}
.dresscode-colors {
  margin: 30px 0;
  display: flex;
  row-gap: 30px;
  column-gap: 30px;
  width: 100%;
  padding: 0;
  list-style: none;

  @media (max-width: 550px) {
    row-gap: 20px;
    column-gap: 20px;
  }

  @media (max-width: 415px) {
    row-gap: 15px;
    column-gap: 15px;
  }
}
.dresscode-color {
  width: 100%;
  border-radius: 50%;

  &::after {
    content: "";
    padding-top: 100%;
    display: block;
  }

  &.color- {
    &1 {
      background-color: #feb6b7;
    }
    &2 {
      background-color: #fee1d1;
    }
    &3 {
      background-color: #ffe7e3;
    }
    &4 {
      background-color: #ebd8b0;
    }
    &5 {
      background-color: #fd9677;
    }
    &6 {
      background-color: #fbc0a0;
    }
    &7 {
      background-color: #ffe1bb;
    }
    &8 {
      background-color: #e6d2d3;
    }
    &9 {
      background-color: #d4b1d1;
    }
    &10 {
      background-color: #5689b8;
    }
    &11 {
      background-color: #a3dbea;
    }
    &12 {
      background-color: #abc6e3;
    }
    &13 {
      background-color: #7e5946;
    }
    &14 {
      background-color: #332522;
    }
  }
}
.dresscode-description {
  display: flex;
  flex-direction: column;
  align-items: center;
  row-gap: 10px;
}
</style>