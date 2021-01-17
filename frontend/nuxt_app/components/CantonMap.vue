<template>
<v-container>
    <p v-if="$fetchState.pending">fetching map data...</p>
    <p v-else-if="$fetchState.error">{{ $fetchState.error.message }}</p>
    <p v-else>data loaded
    </p>
    <v-img id="map"></v-img>
</v-container>
</template>
<script>
import * as d3 from "d3";

export default {
    data() {
        return {
            mapData: undefined,
            canton: undefined,
            currentCanton: undefined,
        }
    },
    async fetch() {
        try {
            const mapData = await this.$axios.$get('/locations/cantons/')
            this.mapData = mapData
            this.generateMap()
        } catch(error) {
            throw new Error('Failed to fetch mapData from /locations/cantons')
        }
    },
    // computed() {
    //     //this.generateMap()
    // },
    methods: {
        // selectCanton(canton) {
        //     this.canton = canton
        // },
        generateMap() {
            // settings
            var width = 960;
            var height = 500;

            var projection = d3.geoMercator()
                .fitSize([width, height], this.mapData)

            var geoGenerator = d3.geoPath()
                .projection(projection);

            // viewbox responsive
            var svg = d3
                .select("#map")
                .append("svg")
                .attr("viewBox", [0, 0, width, height]);

            svg.selectAll("path")
                .data(this.mapData.features)

            .enter()
                .append("path")
                .attr("d", geoGenerator)
                .attr('class', 'stroke')
        }

    },

}
</script>
<style>
.stroke {
    stroke: #005bad;
    stroke-width: 1px;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-dasharray: 0.5;
    fill: white;
}
</style>
