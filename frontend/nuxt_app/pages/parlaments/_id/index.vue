<template>
    <v-card class="mt-3">
        <Overview :parlament="selectedParlament"></Overview>
    </v-card>
</template>
<script>
import {mapState} from 'vuex'
import Overview from '~/components/parlaments/Overview.vue'

export default {
    computed: {
        ...mapState({
            selectedParlament: state => state.parlaments.selectedParlament
        })
    },
    components: {
        Overview,
    },
    middleware: ['auth'],
    layout: 'ParlamentDetail',
}
</script>