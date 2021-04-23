<template>

    <v-container ma-0 mt-3 pa-0>
        <v-row>
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                <AffairsChart :affairs="affairs"></AffairsChart>
            </v-col>

            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                <!-- <FractionsChart :fractions="fractions"></FractionsChart> -->
            </v-col>
        </v-row>
    </v-container>

</template>
<script>
import AffairsChart from '~/components/parlaments/AffairsChart.vue'


export default {
    async asyncData({params, $axios}) {
        const affairs = await $axios.$get(`/parlaments/${params.id}/affairs/`)
        return { 
            affairs: affairs,
        }
    },
    components: {
        AffairsChart,
    },
    middleware: ['auth'],
    layout: 'ParlamentDetail',
}
</script>