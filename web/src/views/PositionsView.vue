<template>
    <div class="d-flex justify-content-center p-5">
        <MapComponent/>
    </div>
</template>
<script>

import MapComponent from '@/components/MapComponent';

export default {
    name: "PositionsView",
    components: {MapComponent},
    data() {
        return {
            positionsList: []
        }
    },
}
</script>