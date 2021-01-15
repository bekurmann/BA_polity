<template>
<v-container>

    <v-row>
        <v-col>
            <v-img id="map" />
        </v-col>
    </v-row>

</v-container>
</template>
<script>
import * as d3 from "d3";

export default {
    data() {
        return {
            mapData: '',
        }
    },
    created() {
        //this.getMapData();
    },
    mounted() {
        this.generateMap();
        
    },
    methods: {
        async getMapData () {
            try {
                const APIdata = await this.$axios.$get('/locations/cantons/')
                this.mapData = APIdata
            } catch(error) {
                console.log(error)
            }
        },
        generateMap() {
            // id & viewbox responsive
            const svg = d3
                .select("#map")
                .append("svg")
                .attr("viewBox", "0 0 960 500")
            
        }
    },
}
</script>