<template>
    <div>
        <div>
            <MapSVG class="map-svg" />
        </div>
    </div>
</template>
  
<script>
import MapSVG from '@/components/MapSVG';

export default {
    name: 'MapComponent',
    components: { MapSVG }
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