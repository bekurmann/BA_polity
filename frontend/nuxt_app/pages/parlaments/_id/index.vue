<template>

        <v-card class="mt-3">
            <v-card-title primary-title>
                Just Testing {{selectedParlament.id}}
                <!-- {{parlament.title}} -->
                <v-avatar
                    size="50"
                >
                <!-- <v-img :src="parlament.jurisdiction_canton.emblem" max-height="30" contain alt="canton emblem"></v-img> -->
                </v-avatar>
            </v-card-title>
        </v-card>

</template>
<script>
import {mapState} from 'vuex'

export default {
    async fetch() {
        try {
            const parlamentData = await this.$axios.$get(`/parlaments/${this.$route.params.id}`);
            this.$store.dispatch("parlaments/setSelectedParlament", parlamentData);
        } catch(error) {
            throw new Error(`Failed to fetch parlamentData from /parlaments/${this.$route.params.id}`)
        }
    },
    computed: {
        ...mapState({
            selectedParlament: state => state.parlaments.selectedParlament
        })
    },
    middleware: ['auth'],
    layout: 'parlaments',
}
</script>