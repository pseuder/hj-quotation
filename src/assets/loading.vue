<style>
.loading {
  position: fixed;
  left: 0;
  top: 0;
  background: url('~@/assets/Spinner-1s-200px.svg') center center no-repeat #fff;
  width: 100vw;
  height: 100vh;
  z-index: 1000;
}
</style>
<template>
  <div class="loading"></div>
</template>

<script>
export default {
  name: 'loading',
}
</script>

