<template>

    <svg></svg>

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
    async fetch({$axios}) {
        const mapData = await this.$axios.$get('/locations/cantons/')
        this.mapData = mapData
    },
    methods: {
        selectCanton(canton) {
            this.canton = canton
        },
        openInfo(canton) {
            this.currentCanton = canton
        },
        closeInfo() {
            this.currentCanton = undefined
        },

    },
    created: {
        createMap () {
            let centered = undefined
            let mapCenter = {
                lat: 1.4,
                lng: 117.5
            };
            let size = {
                height: 700,
                width: d3.select('.map-wrapper').node().getBoundingClientRect().width,
            };
            let color = d3.scale.linear()
                .domain([1,20])
                .clamp(true)
                .range(['#ff0000', '#dddddd']);
            let projection = d3.geo.equirectangular()
                .scale(1400)
                .center([mapCenter.lng, mapCenter.lat])
                .translate([size.width / 2, size.height / 2]);
            let path = d3.geo.path()
                .projection(projection);
            let svg = d3.select('svg')
                .attr('width', size.width)
                .attr('height', size.height);
            
            // add background
            svg.append('rect')
                .attr('class', 'background')
                .attr('width', size.width)
                .attr('height', size.height)
                .on('click', clicked);

            let g = svg.append('g');

            let effectLayer = g.append('g')
                .classed('effect-layer', true);
            let mapLayer = g.append('g')
                .classed('map-layer', true);

            // Load map data
            var features = this.mapData.features;

            // Update color scale domain based on data
            color.domain([0, d3.max(features, nameLength)]);

            // Draw each province as a path
            mapLayer.selectAll('path')
                .data(features)
                .enter().append('path') 
                .attr('d', path)
                .attr('vector-effect', 'non-scaling-stroke')
                .style('fill', fillFn)
                .on('mouseover', mouseover)
                .on('mouseout', mouseout)
                .on('click', clicked);
            

            function clicked(d) {
            var x, y, k;

            // Compute centroid of the selected path
            if (d && centered !== d) {
                var centroid = path.centroid(d);
                x = centroid[0];
                y = centroid[1];
                k = 4;
                centered = d;
                app.openInfo(d.properties);
            } else {
                x = size.width / 2;
                y = size.height / 2;
                k = 1;
                centered = null;
                app.closeInfo();
            }

            // Highlight the clicked province
            mapLayer.selectAll('path')
                .style('fill', function(d){
                return centered && d===centered ? '#D5708B' : fillFn(d);
            });

            // Zoom
            g.transition()
                .duration(750)
                .attr('transform', 'translate(' + size.width / 2 + ',' + size.height / 2 + ')scale(' + k + ')translate(' + -x + ',' + -y + ')');
            }

            function mouseover(d){
            // Highlight hovered province
            d3.select(this).style('fill', '#1483ce');
            if(d) {
                app.selectProvince(d.properties);
            }
            }

            function mouseout(d){
            app.selectProvince(undefined);
            // Reset province color
            mapLayer.selectAll('path')
                .style('fill', (d) => {
                return centered && d===centered ? '#D5708B' : fillFn(d);
                });
            }

            // Get province name length
            function nameLength(d){
            const n = nameFn(d);
            return n ? n.length : 0;
            }

            // Get province name
            function nameFn(d){
            return d && d.properties ? d.properties.name : null;
            }

            // Get province color
            function fillFn(d){
            return color(nameLength(d));
            }
            
        }
    },
}
</script>