<template>
  <router-view></router-view>
</template>

<script>
export default {
  name: 'App',
  watch: {
    '$route'(to) {
      document.title = to.meta.title || to.params[to.meta.paramKey] || to.meta.label || 'Projekt Pos'
    }
  }
}
</script>

<style lang="scss">
@import 'assets/scss/style';

body p-app {
  height: 100vh !important;
}
</style>