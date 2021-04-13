<template>
    <v-card class="mt-3">
        <Members :memberships="memberships"></Members>
    </v-card>
    
</template>
<script>
import Members from '~/components/parlaments/Members.vue'

export default {
    async asyncData({params, $axios}) {
        const memberships = await $axios.$get(`/parlaments/${params.id}/memberships/`)
        return { 
            memberships: memberships,
        }
    },
    components: {
        Members
    },
    middleware: ['auth'],
    layout: 'ParlamentDetail',
}
</script>