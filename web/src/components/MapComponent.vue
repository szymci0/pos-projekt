<template>
    <div>
        <div>
            <MapSVG @click="handleClick($event)" class="map-svg" />
        </div>
    </div>
</template>
  
<script>
import MapSVG from '@/components/MapSVG';
import { countyService } from '@/services/county';

export default {
    name: 'MapComponent',
    components: { MapSVG },
    methods: {
        async handleClick(e) {
            const name = await countyService.getCountyByTeryt(e.target.id);
            this.$emit('county-click', name, e.target.id);
        },
    }
}
</script>
  
<style lang="scss">
.map-svg {
    svg {
        height: 100px;
    }
    path {
        stroke: #000000;
        stroke-width: 0.28346457;
        fill: green;
        stroke-miterlimit: 50;
        stroke-dasharray: none;
        stroke-opacity: 1;
    }
    path:hover {
        cursor: pointer;
        opacity: 50%;
    }
}
</style>