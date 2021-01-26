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
                    <l-control position="topright">
                        <v-card>
                            <v-card-text>
                                <span><v-avatar size="15" color="blue"></v-avatar> Parlaments</span><br>
                               <span><v-avatar size="15" color="green"></v-avatar> Politicans</span>
                            </v-card-text>
                        </v-card>
                    </l-control>
                    <l-marker :lat-lng="[parlament.location.coordinates[1], parlament.location.coordinates[0]]">
                        <l-popup>
                            <b>{{parlament.title}}</b><br>
                            Mehr erfahren (Link)
                        </l-popup>
                    </l-marker>
                    <l-marker 
                    v-for="membership in filteredMemberships" 
                    :lat-lng="[membership.politican.location.coordinates[1], membership.politican.location.coordinates[0]]" 
                    :key="membership.id"
                    :icon="politicanIcon"
                    >
                        <l-popup>
                            <v-img :src="membership.politican.avatar" max-width="40"></v-img>
                            <b>{{membership.politican.first_name}} {{membership.politican.last_name}}</b><br>
                            Fraktion: <br>
                            Mehr erfahren (Link)
                        </l-popup>
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
                // see: https://github.com/pointhi/leaflet-color-markers
                iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
                shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
                iconSize: [25, 41],
                iconAnchor: [12, 41],
                popupAnchor: [1, -34],
                shadowSize: [41, 41]
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