<template>
    <div class="navbar d-flex justify-content-start align-items-center p-3 gap-2">
        <button v-for="link in navLinks" @click="navigate(link.path)" :key="link.name" class="nav-btn">
            {{ link.name.toUpperCase() }}
        </button>
    </div>
</template>
<script>
import { navigation } from './nav';
export default {
    name: 'NavBar',
    data() {
        return {
            navLinks: navigation,
        }
    },
    methods: {
        navigate(path) {
            this.$router.push({ path: path })
        }
    }
}
</script>
<style lang="scss">
.navbar {
    background-color: #F4D03F;
    background-image: linear-gradient(-132deg, #F4D03F 10%, #16A085 100%);
    background-size: 100%;
    opacity: 80%;
    overflow: hidden;
    width: 101%;
    transition: all 1s linear;
    &:hover {
        transition: all 1s linear;
        background-size: 300%;
    }
}

.nav-btn {
    border: 0;
    background-color: transparent;
    font-weight: bold;
    color: white;

    &:hover {
        transition: all 0.2s linear;
        color: #F4D03F;
    }
}
</style>