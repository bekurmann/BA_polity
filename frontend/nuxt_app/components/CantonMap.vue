<template>
<v-container>
    <p v-if="$fetchState.pending">fetching map data...
        <v-skeleton-loader
        class="mx-auto"
        type="image@3"
        height="500"
        ></v-skeleton-loader>
    </p>
    <p v-else-if="$fetchState.error">{{ $fetchState.error.message }}</p>
    <p v-else>data loaded
    </p>
    <v-img id="map" max-height="600"></v-img>
    <v-tooltip bottom v-model="toolTipCanton" 
        :activator="`${ `#` + hoverCanton.id }`" v-if="hoverCanton">
        <span>{{ 'toolTipCanton!' }}</span>
    </v-tooltip>
</v-container>
</template>
<script>
import * as d3 from "d3";

export default {
    data() {
        return {
            mapData: undefined,
            toolTipCanton: false,
            hoverCanton: undefined,
            selectedCanton: undefined,
        }
    },
    async fetch() {
        try {
            const mapData = await this.$axios.$get('/locations/cantons/')
            this.mapData = mapData
            // generate map (after request)
            this.generateMap()
        } catch(error) {
            throw new Error('Failed to fetch mapData from /locations/cantons OR build map')
        }
    },
    methods: {
        onCantonHover(d) {
            this.toolTipCanton = true;
            this.hoverCanton = d.properties.name;
        },
        offCantonHover() {
            this.toolTipCanton = false;
            this.hoverCanton = undefined;
        },
        onCantonClicked(d) {
            this.selectedCanton = d.properties.name;
        },
        generateMap() {
            // settings
            var width = 750;
            var height = 450;

            var projection = d3.geoMercator()
                .fitSize([width, height], this.mapData)

            var geoGenerator = d3.geoPath()
                .projection(projection);

            // viewbox responsive
            var svg = d3
                .select("#map")
                .append("svg")
                .attr("viewBox", [0, 0, width, height]);

            const self=this;

            const cantons = svg.selectAll("path")
                .data(this.mapData.features)
                .enter()
                .append("path")
                .attr("d", geoGenerator)
                // styling
                .attr('class', 'canton')
                // enter data from geojson (properties)
                .attr("id", function(d) { return d.id; })
                // interactions
                .on("mouseover", function(d) { self.onCantonHover(d); } )
                .on("mouseout", function()  { self.offCantonHover(); } )
                .on("click", function(d) { self.onCantonClicked(d); });
        },
    },

}
</script>
<style>
.canton {
    stroke:white;
    stroke-width: 1px;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-dasharray: 0.5;
    fill: #dddddd;
}
.canton:hover {
    fill: #005bad;
}
</style>
