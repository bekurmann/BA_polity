<template>
    <v-container fluid>
        <v-row>
            <v-col cols="12">
                <v-card dark color="primary">
                    <v-card-title primary-title>
                        {{parlament.title}}
                        <v-avatar
                            size="50"
                        >
                        <v-img :src="parlament.jurisdiction_canton.emblem" max-height="30" contain alt="canton emblem"></v-img>
                        </v-avatar>
                    </v-card-title>
                    <v-card-subtitle>{{parlament.number_of_seats}} Seats</v-card-subtitle>
                </v-card>
            </v-col>
        </v-row>
        <!-- start grid -->
        <v-row>
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6" class="d-flex child-flex align-stretch">
                <ParlamentDetailGeneralInformation :parlament="parlament"></ParlamentDetailGeneralInformation>
            </v-col>
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6" class="d-flex child-flex align-stretch"> 
                <ParlamentDetailContact :parlament="parlament"></ParlamentDetailContact>
            </v-col>
            <v-col cols="12" xs="12" sm="12" md="12" lg="12" xl="12" class="d-flex child-flex align-stretch">

                <v-card v-if="$fetchState.pending">
                    <v-card-title primary-title>
                        Map
                    </v-card-title>
                    <v-card-text>
                        <v-skeleton-loader
                        class="mx-auto"
                        type="image@2"
                        ></v-skeleton-loader>
                    </v-card-text>
                </v-card>

                <p v-else-if="$fetchState.error">{{ $fetchState.error.message }}</p>
                <ParlamentDetailMap :parlament="parlament" :memberships="memberships" v-else></ParlamentDetailMap>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                <v-card>
                    <v-card-title primary-title>
                        Affairs
                    </v-card-title>
                </v-card>
            </v-col>
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                <ParlamentDetailMembers :memberships="memberships"></ParlamentDetailMembers>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                <v-card>
                    <v-card-title primary-title>
                        Sessions
                    </v-card-title>
                    
                </v-card>
            </v-col>
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                <v-card>
                    <v-card-title primary-title>
                        Commissions
                    </v-card-title>
                </v-card>
            </v-col>
        </v-row>
        <!-- end grid -->
        
    </v-container>
</template>
<script>
import ParlamentDetailGeneralInformation from '~/components/parlaments/ParlamentDetailGeneralInformation.vue'
import ParlamentDetailContact from '~/components/parlaments/ParlamentDetailContact.vue'
import ParlamentDetailMap from '~/components/parlaments/ParlamentDetailMap.vue'
import ParlamentDetailMembers from '~/components/parlaments/ParlamentDetailMembers.vue'

export default {
    async asyncData({params, $axios}) {
        const parlament = await $axios.$get(`/parlaments/${params.id}`)
        const memberships = await $axios.$get(`/parlaments/${params.id}/memberships/`)
        return { 
            parlament: parlament,
            memberships: memberships,
        }
    },
    async fetch() {
        try {
            this.ParlamentMap
        } catch(error) {
            throw new Error('Failed to fetch parlamentMap (dependencies)')
        }
    },
    components: {
        ParlamentDetailGeneralInformation,
        ParlamentDetailContact,
        ParlamentDetailMap,
        ParlamentDetailMembers,
    },
    middleware: ['auth']
}
</script>