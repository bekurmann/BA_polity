<template>

    <v-container ma-0 mt-3 pa-0>
        <v-row>
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6" class="d-flex child-flex align-stretch">
                <Fractions :fractions="fractions"></Fractions>
            </v-col>

            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6" class="d-flex child-flex align-stretch">
                <FractionsChart :fractions="fractions"></FractionsChart>
            </v-col>
        </v-row>
    </v-container>

</template>
<script>
import Fractions from '~/components/parlaments/Fractions.vue'
import FractionsChart from '~/components/parlaments/FractionsChart.vue'


export default {
    async asyncData({params, $axios}) {
        const fractions = await $axios.$get(`/parlaments/${params.id}/fractions/`)
        return { 
            fractions: fractions,
        }
    },
    components: {
        Fractions,
        FractionsChart,
    },
    middleware: ['auth'],
    layout: 'ParlamentDetail',
}
</script>