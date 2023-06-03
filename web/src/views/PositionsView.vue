<template>
    <div class="d-flex flex-column justify-content-start align-items-center p-5">
        <h2>{{ countyName }}</h2>
        <MapComponent
            @county-click="setCounty"
        />
    </div>
</template>
<script>

import MapComponent from '@/components/MapComponent';

export default {
    name: "PositionsView",
    components: {MapComponent},
    data() {
        return {
            countyName: 'Click to display county name'
        }
    },
    methods: {
        setCounty(name) {
            this.countyName = name;
        }
    }
}
</script>