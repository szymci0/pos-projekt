<template>
    <div class="p-app">
        <NavBar/>
        <div class="p-body">
            <main class="p-main">
                <router-view :key="$route.path"></router-view>
            </main>
        </div>
        <div class="p-footer">
            <span>Projekt POS 2023</span>
        </div>
    </div>
</template>
<script>
import { ActiveUser } from '@/services/user';
import NavBar from '@/containers/NavBar'
export default {
    name: 'MainContainer',
    components: { NavBar},
    data() {
        return {
            user: {}
        }
    },
    async mounted() {
        this.user = ActiveUser.get();
    }

}
</script>