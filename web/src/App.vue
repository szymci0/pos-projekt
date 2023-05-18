<template>
  <router-view></router-view>
</template>

<script>
export default {
  name: 'App',
  watch: {
    '$route'(to) {
      console.log(this.$route);
      document.title = to.meta.title || to.params[to.meta.paramKey] || to.meta.label || 'Projekt Pos'
    }
  }
}
</script>

<style lang="scss">
@import 'assets/scss/style';

</style>