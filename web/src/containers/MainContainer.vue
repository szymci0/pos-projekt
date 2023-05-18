<template>
    <div class="p-app">
        <div class="p-header">
            <span>header {{ user.email }}</span>
        </div>
        <div class="p-body">
            <main class="p-main">
                <router-view :key="$route.path"></router-view>
            </main>
        </div>
        <div class="p-footer">
            <span>footer</span>
        </div>
    </div>
</template>
<script>
import { ActiveUser } from '@/services/user';

export default {
    name: 'MainContainer',
    data() {
        return {
            user: {}
        }
    },
    mounted() {
        this.user = ActiveUser.get();
    }

}
</script>