<template>
    <v-card class="mt-3">
        <ParlamentDetailMembers :memberships="memberships"></ParlamentDetailMembers>
    </v-card>
    
</template>
<script>
import ParlamentDetailMembers from '~/components/parlaments/ParlamentDetailMembers.vue'

export default {
    async asyncData({params, $axios}) {
        const memberships = await $axios.$get(`/parlaments/${params.id}/memberships/`)
        return { 
            memberships: memberships,
        }
    },
    components: {
        ParlamentDetailMembers
    },
    middleware: ['auth'],
    layout: 'parlaments',
}
</script>