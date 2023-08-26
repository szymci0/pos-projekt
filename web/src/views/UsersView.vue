<template>
    <div class="d-flex justify-content-center align-items-cente">
        <v-client-table :data="usersData" :columns="columns">

        </v-client-table>
    </div>
</template>
<script>
import { countyService } from '@/services/county';

export default {
    name: "UsersView",
    async mounted() {
        await this.fetchUsersData();
    },
    data() {
        return {
            usersData: [],
            columns: ["county", "users"]
        }
    },
    methods: {
        async fetchUsersData() {
            this.usersData = await countyService.getUsers();
        }
    }
}
</script>