<template>
    <v-card class="mt-3">
        <Overview :parlament="selectedParlament"></Overview>
    </v-card>
</template>
<script>
import {mapState} from 'vuex'
import Overview from '~/components/parlaments/Overview.vue'

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
    components: {
        Overview,
    },
    middleware: ['auth'],
    layout: 'parlaments',
}
</script>