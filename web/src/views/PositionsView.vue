<template>
    <div class="d-flex flex-column justify-content-start align-items-center p-5">
        <h2>{{ countyName }}</h2>
        <input v-model="nameSearch" placeholder="County Name" type="text"/>
        <div class="d-flex justify-content-start gap-1">
            <button @click="handleSearch">Search</button>
            <button @click="clearSearch">Reset</button>
        </div>
        <MapComponent
            @county-click="setCounty"
        />
    </div>
</template>
<script>

import MapComponent from '@/components/MapComponent';
import { countyService } from '@/services/county';

export default {
    name: "PositionsView",
    components: {MapComponent},
    data() {
        return {
            countyName: 'Click to display county name',
            nameSearch: '',
            name: '',
            teryt: '',
        }
    },
    methods: {
        setCounty(name) {
            this.countyName = name;
        },
        async clearSearch() {
            this.nameSearch = "";
            await this.handleSearch();
            this.teryt = "";
        },
        async handleSearch() {
            if (this.teryt.length) {
                document.getElementById(this.teryt).style.fill = 'green';
            }
            this.name = this.nameSearch;
            if (this.name.length) {
                this.teryt = await countyService.getCountyByName(this.nameSearch);
                document.getElementById(this.teryt).style.fill = 'red';
            }
        }
    }
}
</script>