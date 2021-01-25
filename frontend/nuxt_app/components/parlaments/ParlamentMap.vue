<template>
    <v-card>
        <v-card-title primary-title>
            Map
        </v-card-title>
        <v-card-text>
            <div id="map-wrap" style="height: 350px">
                <client-only>
                <l-map :zoom=10 :center="[parlament.location.coordinates[1], parlament.location.coordinates[0]]">
                    <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
                    <l-marker :lat-lng="[parlament.location.coordinates[1], parlament.location.coordinates[0]]"></l-marker>
                    <l-marker 
                    v-for="membership in filteredMemberships" 
                    :lat-lng="[membership.politican.location.coordinates[1], membership.politican.location.coordinates[0]]" 
                    :key="membership.id"
                    :icon="politicanIcon"
                    >
                    </l-marker>
                </l-map>
                </client-only>
            </div>
        </v-card-text>
    </v-card>
</template>
<script>
import { icon } from "leaflet";

export default {
    data() {
        return {
            politicanIcon: icon({
                iconUrl: 'http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|abcdef&chf=a,s,ee00FFFF',
                iconSize: [22, 30],
                iconAnchor: [10, 40]
            })
        }
    },
    props: {
        parlament: {
            type: Object
        },
        memberships: {
            type: Array
        },
    },
    computed: {
        filteredMemberships: function() {
            let notNullMemberships = this.memberships.filter(el => el.politican.location !== null)
            return notNullMemberships;    
        }
    }
}
</script>