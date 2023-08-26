<template>
    <div class="d-flex flex-column justify-content-start align-items-center p-4">
        <div class="action-bar">
            <h1>COUNTY USERS</h1>
            <button>
                Upload listing file
            </button>
        </div>
        <div class="d-flex justify-content-center align-items-center">
            <v-client-table 
                class="county-users-table" 
                :data="usersData" 
                :columns="columns"
            >

            </v-client-table>
        </div>
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
<style lang="scss">
.county-users-table {
    .table {
        th td {
            background-color: white !important;

        }
    }

    .VuePagination {
        background-color: pink !important;
    }
}
</style>