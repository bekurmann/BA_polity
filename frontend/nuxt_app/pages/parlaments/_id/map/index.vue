<template>
    <v-card class="mt-3">
        <Map :memberships="memberships" :parlament="parlament"></Map>
    </v-card>
    
</template>
<script>
import Map from '~/components/parlaments/Map.vue'

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
        Map
    },
    middleware: ['auth'],
    layout: 'parlaments',
}
</script>