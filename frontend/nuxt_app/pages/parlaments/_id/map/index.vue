<template>
    <v-card class="mt-3">
        <ParlamentDetailMap :memberships="memberships" :parlament="parlament"></ParlamentDetailMap>
    </v-card>
    
</template>
<script>
import ParlamentDetailMap from '~/components/parlaments/ParlamentDetailMap.vue'

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
        ParlamentDetailMap
    },
    middleware: ['auth'],
    layout: 'parlaments',
}
</script>