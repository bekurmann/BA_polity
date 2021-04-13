<template>
    <v-card>
        <v-card-title>Map</v-card-title>
        <v-card-text>
            <div id="map-wrap" style="height: 50vh">
                <client-only>
                <l-map :zoom=10 :center="[politicanDetails.location.coordinates[1], politicanDetails.location.coordinates[0]]" class="lowerZ">
                    <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
                    <l-control position="topright">
                        <v-card>
                            <v-card-text>
                               <span><v-avatar size="15" color="green"></v-avatar> Politican</span>
                            </v-card-text>
                        </v-card>
                    </l-control>
                    <l-marker 
                        :lat-lng="[politicanDetails.location.coordinates[1], politicanDetails.location.coordinates[0]]"
                        :icon="politicanIcon"
                    >
                        <l-popup>
                            <b>{{politicanDetails.first_name}}
                            {{politicanDetails.last_name}}</b><br>
                            {{politicanDetails.street1}}<br>
                            {{politicanDetails.city.name}}<br>
                        </l-popup>
                    </l-marker>
                </l-map>
                </client-only>
            </div>       
        </v-card-text>
    </v-card>
</template>
<script>
export default {
    data() {
        return {
            politicanIcon: this.$L.icon({
                // see: https://github.com/pointhi/leaflet-color-markers
                iconUrl: '/leaflet/greenMarker.png',
                shadowUrl: '/leaflet/markerShadow.png',
                iconSize: [25, 41],
                iconAnchor: [12, 41],
                popupAnchor: [1, -34],
                shadowSize: [41, 41]
            })
        }
    },
    props: {
        politicanDetails: {
            type: Object
        }
    },
}
</script>