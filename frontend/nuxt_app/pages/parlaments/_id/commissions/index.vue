<template>

    <v-container ma-0 mt-3 pa-0>
        <v-row>
            <v-col>
                <Commissions :commissions="commissions"></Commissions>
            </v-col>
        </v-row>
    </v-container>

</template>
<script>
import Commissions from '~/components/parlaments/Commissions.vue'


export default {
    async asyncData({params, $axios}) {
        const commissions = await $axios.$get(`/parlaments/${params.id}/commissions/`)
        return { 
            commissions: commissions,
        }
    },
    components: {
        Commissions,
    },
    middleware: ['auth'],
    layout: 'ParlamentDetail',
}
</script>