<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card>
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
            <v-col cols="12" xs="12" sm="12" md="4" lg="4" xl="4" class="d-flex child-flex align-stretch">
                <ParlamentGeneralInformation :parlament="parlament"></ParlamentGeneralInformation>
            </v-col>
            <v-col cols="12" xs="12" sm="12" md="4" lg="4" xl="4" class="d-flex child-flex align-stretch"> 
                <ParlamentContact :parlament="parlament"></ParlamentContact>
            </v-col>
            <v-col cols="12" xs="12" sm="12" md="4" lg="4" xl="4" class="d-flex child-flex align-stretch">
                <ParlamentMap :parlament="parlament" :memberships="memberships"></ParlamentMap>
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
                <v-card>
                    <v-card-title primary-title>
                        Members
                    </v-card-title>
                </v-card>
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
import ParlamentGeneralInformation from '~/components/parlaments/ParlamentGeneralInformation.vue'
import ParlamentContact from '~/components/parlaments/ParlamentContact.vue'
import ParlamentMap from '~/components/parlaments/ParlamentMap.vue'

export default {
    async asyncData({params, $axios}) {
        const parlament = await $axios.$get(`/parlaments/${params.id}`)
        const memberships = await $axios.$get(`/parlaments/${params.id}/memberships/`)
        return { 
            parlament: parlament,
            memberships: memberships,
        }
    },
    components: {
        ParlamentGeneralInformation,
        ParlamentContact,
        ParlamentMap,

    },
    middleware: ['auth-user']
}
</script>