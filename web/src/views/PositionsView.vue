<template>
    <div>
        <div 
        class="d-flex flex-column align-items-center" 
        v-for="position in positionsList"
        :key="position.x"
        >
            {{ position.email }}
            {{ position.x }}
            {{ position.y }}
        </div>
        <MapComponent/>
    </div>
</template>
<script>
import { positionService } from '@/services/positions';
import MapComponent from '@/components/MapComponent';

export default {
    name: "PositionsView",
    components: {MapComponent},
    data() {
        return {
            positionsList: []
        }
    },
    async mounted() {
        this.positionsList = await positionService.getPositions();
    }
}
</script>