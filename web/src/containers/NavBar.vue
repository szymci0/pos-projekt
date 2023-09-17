<template>
    <div class="navbar d-flex justify-content-between align-items-center p-3 gap-2">
        <div class="d-flex align-items-center">
            <button v-for="link in navLinks" @click="navigate(link.path)" :key="link.name" class="nav-btn">
                {{ link.name.toUpperCase() }}
            </button>
        </div>
        <div>
            <button 
                class="nav-btn" 
                @click="logOut"
                data-cy="logout"
            >
                Log Out
            </button>
        </div>
    </div>
</template>
<script>
import { navigation } from './nav';
import { ActiveUser } from '@/services/user';

export default {
    name: 'NavBar',
    data() {
        return {
            navLinks: navigation,
        }
    },
    methods: {
        logOut() {
            ActiveUser.clear();
            window.location.reload();
        },
        navigate(path) {
            this.$router.push({ path: path })
        }
    }
}
</script>
<style lang="scss">
.navbar {
    background-color: #006A4E;
    background-size: 100%;
    opacity: 80%;
    overflow: hidden;
    width: 101%;
    transition: all 1s linear;
    border-bottom: 10px solid #F4D03F;
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