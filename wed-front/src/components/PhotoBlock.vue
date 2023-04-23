<template>
  <div id="photo" class="photo">
    <p>Скоро здесь появятся фотографии с торжества</p>
    <div class="loader"></div>
  </div>
</template>

<style scoped lang="scss">
.photo {
  color: #855f5f;
  font-size: 24px;
  text-align: center;
  margin: 40px auto;

  @media (max-width: 768px) {
    margin-top: 20px;
    font-size: 18px;
  }
}
.loader {
  border: 10px solid #f3f3f3;
  border-radius: 50%;
  border-top: 10px solid #feb6b7;
  width: 80px;
  height: 80px;
  -webkit-animation: spin 2s linear infinite; 
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
</style>