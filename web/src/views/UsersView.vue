<template>
    <div class="d-flex flex-column justify-content-start align-items-center p-4">
        <UploadModal
            :show="showUpload"
            title="Upload listing file"
            @close="showUpload = false"
        />
        <div class="action-bar">
            <h1>COUNTY USERS</h1>
            <button @click="showUpload = true">
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
import UploadModal from '@/components/UploadModal';

export default {
    name: "UsersView",
    components: {UploadModal},
    async mounted() {
        await this.fetchUsersData();
    },
    data() {
        return {
            usersData: [],
            columns: ["county", "users"],
            showUpload: false,
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