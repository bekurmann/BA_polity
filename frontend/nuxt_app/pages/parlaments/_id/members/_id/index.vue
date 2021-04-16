<template>
    <!-- header with avatar-->
    <v-container ma-0 mt-3 pa-0 v-if="$fetchState.pending">
        <v-row>
            <v-col>
                <v-skeleton-loader
                class="mx-auto"
                type="article@2"
                ></v-skeleton-loader>
            </v-col>
        </v-row>
    </v-container>
    <v-container ma-0 mt-3 pa-0 v-else>
        <v-row>
            <v-col cols="12" xs="12" sm="6" md="6" lg="6" xl="6" class="d-flex child-flex align-stretch">
                <Overview :politicanDetails="politicanDetails"></Overview>
            </v-col>
            <v-col cols="12" xs="12" sm="6" md="6" lg="6" xl="6" class="d-flex child-flex align-stretch">
                <Map :politicanDetails="politicanDetails"></Map>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" xs="12" sm="12" md="12" lg="12" xl="12">
                <Memberships :politicanDetails="politicanDetails"></Memberships>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" xs="12" sm="12" md="12" lg="12" xl="12">
                <Affairs :politicanDetails="politicanDetails"></Affairs>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" xs="12" sm="12" md="12" lg="12" xl="12">
                <DebateStatements :politicanDetails="politicanDetails"></DebateStatements>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import Overview from '~/components/politicans/Overview.vue'
import Map from '~/components/politicans/Map.vue'
import Memberships from '~/components/politicans/Memberships.vue'
import Affairs from '~/components/politicans/Affairs.vue'
import DebateStatements from '~/components/politicans/DebateStatements.vue'

export default {
    data() {
        return {
            politicanDetails: {}
        }
    },
    async fetch() {
        try {
            const politicanDetails = await this.$axios.$get(`/politicans/${this.$route.params.id}`)
            this.politicanDetails = politicanDetails
        } catch(error) {
            throw new Error(`Failed to fetch politicanDetails from /politicans/${this.$route.params.id}`)
        }
    },
    components: {
        Overview,
        Map,
        Memberships,
        Affairs,
        DebateStatements,
    },
    middleware: ['auth'],
    layout: 'ParlamentDetail',
}
</script>