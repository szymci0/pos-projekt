<template>
    <div class="d-flex flex-column justify-content-start align-items-center p-5">
        <h2>{{ countyName }}</h2>
        <input v-model="nameSearch" placeholder="County Name" type="text" />
        <div class="d-flex justify-content-start gap-1">
            <button @click="handleSearch">Search</button>
            <button @click="clearSearch">Reset</button>
        </div>
        <MapComponent @county-click="setCounty" />
    </div>
</template>
<script>

import MapComponent from '@/components/MapComponent';
import { COUNTY_ENDPOINTS } from '@/services/county';
import { request } from '@/utils/request';

export default {
    name: "PositionsView",
    components: { MapComponent },
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
            this.nameSearch = "";
            this.setColor('green');
            this.teryt = [];
        },
        setColor(color) {
            this.teryt.forEach((code) => {
                document.getElementById(code).style.fill = color;
            });
        },
        async fetchTeryt() {
            const { res, data } = await request({
                url: COUNTY_ENDPOINTS.by_name(this.nameSearch)
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
                await this.fetchTeryt()
            }
            else {
                this.setColor('green');
                alert("You must fill the county name!");
            }
        }
    }
}
</script>