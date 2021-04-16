<template>
    <v-card>
        <v-card-title primary-title>
            Map
        </v-card-title>
        <v-card-text>
            <div id="map-wrap" style="height: 55vh">
                <client-only>
                <l-map :zoom=10 :center="[parlament.location.coordinates[1], parlament.location.coordinates[0]]" class="lowerZ">
                    <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
                    <l-control position="topright">
                        <v-card>
                            <v-card-text>
                                <span><v-avatar size="15" color="blue"></v-avatar> Parlaments</span><br>
                                <span><v-avatar size="15" color="green"></v-avatar> Politicans (active)</span><br>
                                <span><v-avatar size="15" color="red"></v-avatar> Politicans (inactive)</span>
                            </v-card-text>
                        </v-card>
                    </l-control>
                    <l-marker :lat-lng="[parlament.location.coordinates[1], parlament.location.coordinates[0]]">
                        <l-popup>
                            <b>{{parlament.title}}</b><br>
                            Mehr erfahren (Link)
                        </l-popup>
                    </l-marker>
                    <!-- active politicans -->
                    <l-marker 
                    v-for="membership in filteredMemberships_active" 
                    :lat-lng="[membership.politican.location.coordinates[1], membership.politican.location.coordinates[0]]" 
                    :key="membership.id"
                    :icon="politicanIcon_active"
                    >
                        <l-popup>
                            <v-img :src="membership.politican.avatar" max-width="40"></v-img>
                            <b>{{membership.politican.first_name}} {{membership.politican.last_name}}</b><br>
                            <NuxtLink :to="'/parlaments/' + selectedParlament.id + '/members/' +membership.politican.id">Mehr erfahren (Link)</NuxtLink>
                        </l-popup>
                    </l-marker>
                    <!-- inactive politicans -->
                    <l-marker 
                    v-for="membership in filteredMemberships_inactive" 
                    :lat-lng="[membership.politican.location.coordinates[1], membership.politican.location.coordinates[0]]" 
                    :key="membership.id"
                    :icon="politicanIcon_inactive"
                    >
                        <l-popup>
                            <v-img :src="membership.politican.avatar" max-width="40"></v-img>
                            <b>{{membership.politican.first_name}} {{membership.politican.last_name}}</b><br>
                            <NuxtLink :to="'/parlaments/' + selectedParlament.id + '/members/' +membership.politican.id">Mehr erfahren (Link)</NuxtLink>
                        </l-popup>
                    </l-marker>
                </l-map>
                </client-only>
            </div>
        </v-card-text>
    </v-card>
</template>
<script>
import {mapState} from 'vuex'

export default {
    data() {
        return {
            politicanIcon_active: this.$L.icon({
                // see: https://github.com/pointhi/leaflet-color-markers
                iconUrl: '/leaflet/greenMarker.png',
                shadowUrl: '/leaflet/markerShadow.png',
                iconSize: [25, 41],
                iconAnchor: [12, 41],
                popupAnchor: [1, -34],
                shadowSize: [41, 41]
            }),
            politicanIcon_inactive: this.$L.icon({
                iconUrl: '/leaflet/redMarker.png',
                shadowUrl: '/leaflet/markerShadow.png',
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
        filteredMemberships_active: function() {
            let notNullMemberships = this.memberships.filter(el => el.politican.location !== null)
            let notNullMemberships_active = notNullMemberships.filter(el => el.active == true)
            return notNullMemberships_active;    
        },
        filteredMemberships_inactive: function() {
            let notNullMemberships = this.memberships.filter(el => el.politican.location !== null)
            let notNullMemberships_inactive = notNullMemberships.filter(el => el.active == false)
            return notNullMemberships_inactive;  
        },
        ...mapState({
        selectedParlament: state => state.parlaments.selectedParlament
        })
    }
}
</script>
<style>
/* leaflet map went over app bar; changed zindex */
.lowerZ {
    z-index: 0;
}
</style>