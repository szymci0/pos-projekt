<template>
    <div class="d-flex flex-column justify-content-start align-items-center p-5">
        <ModalComponent/>
        <div class="action-bar">
            <h1>COUNTIES</h1>
            <div>
                <input v-model="nameSearch" placeholder="Search county" type="text" />
                <button v-if="!this.name.length" @click="handleSearch">
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
import { COUNTY_ENDPOINTS } from '@/services/county';
import { request } from '@/utils/request';

export default {
    name: "PositionsView",
    components: { MapComponent, ModalComponent },
    data() {
        return {
            countyName: 'Click to display county name',
            nameSearch: '',
            name: '',
            teryt: [],
        }
    },
    methods: {
        setCounty(name) {
            this.countyName = name;
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
        }
    }
}
</script>
<style>
.action-bar {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 3em;
    border-bottom: 1px solid yellow;
}
</style>