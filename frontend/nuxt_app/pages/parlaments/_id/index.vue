<template>
    <v-container fluid>
        <v-card dark color="primary">
            <v-card-title primary-title>
                {{parlament.title}}
                <v-avatar
                    size="50"
                >
                <v-img :src="parlament.jurisdiction_canton.emblem" max-height="30" contain alt="canton emblem"></v-img>
                </v-avatar>
            </v-card-title>

            <v-card-text>
                
                <v-tabs
                    v-model="tab"
                    color="primary"
                    light
                    center-active
                    icons-and-text
                    slider-color="primary"
                >
                    <v-tabs-slider></v-tabs-slider>

                    <v-tab href="#tab-1">
                            Overview
                            <v-icon>mdi-view-comfy-outline</v-icon>
                    </v-tab>  

                    <v-tab href="#tab-2">
                            Members
                            <v-icon>mdi-account-multiple-outline</v-icon>
                    </v-tab>  

                    <v-tab href="#tab-3">
                            Affairs
                            <v-icon>mdi-file-document-outline</v-icon>
                    </v-tab>  

                    <v-tab href="#tab-4">
                            Sessions
                            <v-icon>mdi-seat-outline</v-icon>
                    </v-tab>  

                    <v-tab href="#tab-5">
                            Commissions
                            <v-icon>mdi-domain</v-icon>
                    </v-tab>  

                    <v-tab href="#tab-6">
                            Map
                            <v-icon>mdi-map-marker-outline</v-icon>
                    </v-tab> 

                    <v-tab href="#tab-7">
                            Analysis
                            <v-icon>mdi-chart-line-variant</v-icon>
                    </v-tab> 

                    <v-tabs-items v-model="tab">
                        
                        <v-tab-item value="tab-1">
                            <ParlamentDetailGeneralInformation :parlament="parlament"></ParlamentDetailGeneralInformation>
                        </v-tab-item>

                        <v-tab-item value="tab-2">
                            <ParlamentDetailMembers :memberships="memberships"></ParlamentDetailMembers>
                        </v-tab-item>

                        <v-tab-item value="tab-3">
                            <ParlamentDetailGeneralInformation :parlament="parlament"></ParlamentDetailGeneralInformation>
                        </v-tab-item>

                        <v-tab-item value="tab-4">
                            <ParlamentDetailGeneralInformation :parlament="parlament"></ParlamentDetailGeneralInformation>
                        </v-tab-item>

                        <v-tab-item value="tab-5">
                            <ParlamentDetailGeneralInformation :parlament="parlament"></ParlamentDetailGeneralInformation>
                        </v-tab-item>

                        <v-tab-item value="tab-6">
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
                        </v-tab-item>

                        <v-tab-item value="tab-7">
                            <ParlamentDetailGeneralInformation :parlament="parlament"></ParlamentDetailGeneralInformation>
                        </v-tab-item>

                    </v-tabs-items>

                </v-tabs>

            </v-card-text>

        </v-card>        
    </v-container>
</template>
<script>
import ParlamentDetailGeneralInformation from '~/components/parlaments/ParlamentDetailGeneralInformation.vue'
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
        ParlamentDetailMap,
        ParlamentDetailMembers,
    },
    data () {
        return {
            tab: null,
        }
    },
    middleware: ['auth']
}
</script>