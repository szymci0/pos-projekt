<template>
    <div class="d-flex flex-column justify-content-start align-items-center p-4">
        <UploadModal
            :show="showUpload"
            title="Upload listing file"
            @close="closeUploadModal"
            :uploadUrl="`${COUNTY_ENDPOINTS.users}/upload`"
        />
        <div class="action-bar">
            <h1>COUNTY USERS</h1>
            <div class="d-flex gap-2">
                <button @click="downloadTemplate">
                    Download template
                </button>
                <button @click="showUpload = true">
                    Upload listing file
                </button>
            </div>
        </div>
        <div class="d-flex justify-content-center align-items-center">
            <v-client-table 
                class="county-users-table" 
                :data="usersData" 
                :columns="columns"
                :key="refreshTable"
            >

            </v-client-table>
        </div>
    </div>
</template>
<script>
import { countyService, COUNTY_ENDPOINTS } from '@/services/county';
import UploadModal from '@/components/UploadModal';
import { downloadFile } from '@/utils/request';

export default {
    name: "UsersView",
    components: {UploadModal},
    async mounted() {
        await this.fetchUsersData();
    },
    data() {
        return {
            COUNTY_ENDPOINTS,
            usersData: [],
            columns: ["county", "users"],
            showUpload: false,
            refreshTable: 0,
        }
    },
    methods: {
        async fetchUsersData() {
            this.usersData = await countyService.getUsers();
            this.refreshTable += 1;
        },
        async downloadTemplate() {
            await downloadFile({
                downloadURL: COUNTY_ENDPOINTS.users + "/template"
            })
        },
        async closeUploadModal() {
            this.showUpload = false;
            await this.fetchUsersData();
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