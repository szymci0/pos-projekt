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
    </div>
</template>
<script>
import { positionService } from '@/services/positions';
export default {
    name: "PositionsView",
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