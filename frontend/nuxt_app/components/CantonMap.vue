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
    <p v-else>data loaded; {{ selectedCanton.name }}
    </p>

    <v-img id="map" max-height="600"></v-img>

    <v-tooltip right v-model="toolTipCanton" :activator="`${ `#` + hoverCanton.id }`" v-if="hoverCanton">
        <span>fucker!</span>
    </v-tooltip>
    

    <!-- <v-tooltip bottom v-model="toolTipCanton" 
        :activator="`${ `#` + hoverCanton.id }`" v-if="hoverCanton">
        <span>{{ hoverCanton.name }}</span>
    </v-tooltip> -->

</v-container>
</template>
<script>
import * as d3 from "d3";

export default {
    data() {
        return {
            mapData: {},
            toolTipCanton: false,
            hoverCanton: {},
            selectedCanton: {},
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
        generateMap() {
            // settings
            var width = 750;
            var height = 450;
            let self=this;

            var projection = d3.geoMercator()
                .fitSize([width, height], this.mapData)

            var geoGenerator = d3.geoPath()
                .projection(projection);

            // viewbox responsive
            var svg = d3
                .select("#map")
                .append("svg")
                .attr("viewBox", [0, 0, width, height]);

            const cantons = svg.selectAll("path")
                .data(this.mapData.features)
                .enter()
                .append("path")
                .attr("d", geoGenerator)
                // styling
                .attr('class', 'canton')
                // enter data from geojson (properties)
                .attr("id", function(d) { return d.id; });
                // interactions
            cantons.on("mouseover", function(event, d) { self.onCantonHover(d); } );
            cantons.on("mouseout", function()  { self.offCantonHover(); } );
            cantons.on("click", function(event, d) { self.onCantonClicked(d); });
        },
        onCantonHover(d) {
            console.log(d);
            this.toolTipCanton = true;
            this.hoverCanton = d.properties;
        },
        offCantonHover() {
            this.toolTipCanton = false;
            this.hoverCanton = undefined;
        },
        onCantonClicked(d) {
            this.selectedCanton = d.properties;
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
