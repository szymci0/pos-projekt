<template>
    <div class="d-flex flex-column justify-content-start align-items-center p-4">
        <ModalComponent 
            title="Add user to county" 
            :key="showModal" 
            :show="showModal" 
            @close="showModal = false"
        >
            <template #body>
                <input v-model="addEmail" type="text" placeholder="Email"/>
                <span data-cy="selected-county">Selected county: {{ countyName }}</span>
            </template>
            <template #footer>
                <button @click="addUserToCounty">Add user</button>
            </template>
        </ModalComponent>
        <div class="action-bar">
            <h1>COUNTIES</h1>
            <div>
                <input v-model="nameSearch" placeholder="Search county" type="text" data-cy="county-search" />
                <button v-if="!this.name.length" @click="handleSearch" data-cy="search-button">
                    Search
                </button>
                <button v-else @click="clearSearch">
                    Reset
                </button>
            </div>
        </div>
        <MapComponent @county-click="setCounty" />
    </div>
</template>
<script>

import MapComponent from '@/components/MapComponent';
import ModalComponent from '@/components/ModalComponent.vue';
import { COUNTY_ENDPOINTS, countyService } from '@/services/county';
import { request } from '@/utils/request';

export default {
    name: "CountyView",
    components: { MapComponent, ModalComponent },
    data() {
        return {
            countyName: 'Click to display county name',
            nameSearch: '',
            name: '',
            teryt: [],
            showModal: false,
            selectedTeryt: '',
            addEmail: '',
        }
    },
    methods: {
        setCounty(name, teryt) {
            this.countyName = name;
            this.selectedTeryt = teryt;
            this.showModal = true;
        },
        async clearSearch() {
            this.name = ""
            this.nameSearch = "";
            this.setColor('green');
            this.teryt = [];
        },
        setColor(color) {
            this.teryt.forEach((code) => {
                document.getElementById(code).style.fill = color;
            });
        },
        async fetchTeryt(name) {
            const { res, data } = await request({
                url: COUNTY_ENDPOINTS.by_name(name)
            });
            if (res.status !== 200) {
                return alert('County not found!')
            }

            this.teryt = data;

            if (this.teryt.length) {
                this.setColor('red')
            }
        },
        async handleSearch() {
            this.name = this.nameSearch;
            if (this.name.length) {
                await this.fetchTeryt(this.name)
            }
            else {
                this.clearSearch();
                alert("You must fill the county name!");
            }
        },
        async addUserToCounty() {
            const res = await countyService.addUser(this.selectedTeryt, this.addEmail);
            if (res.status !== 200) {
                return alert("Something went wrong!")
            }
            this.selectedTeryt = "";
            this.addEmail = "";
            this.showModal = false;
        }
    }
}
</script>