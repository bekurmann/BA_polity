<template>

    <v-container ma-0 mt-3 pa-0>
        <v-row>
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                <AnalysisParlamentAffairsPerYearOW :numberOfAffairsPerYear="numberOfAffairsPerYear"></AnalysisParlamentAffairsPerYearOW>
            </v-col>

            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                <!-- <FractionsChart :fractions="fractions"></FractionsChart> -->
            </v-col>
        </v-row>
    </v-container>

</template>
<script>
import AnalysisParlamentAffairsPerYearOW from '~/components/analysis/AnalysisParlamentAffairsPerYearOW.vue'


export default {
    async asyncData({params, $axios}) {
        const numberOfAffairsPerYear = await $axios.$get(`/analysis/ow/data/`)
        return { 
            numberOfAffairsPerYear: numberOfAffairsPerYear,
        }
    },
    components: {
        AnalysisParlamentAffairsPerYearOW,
    },
    middleware: ['auth'],
    layout: 'ParlamentDetail',
}
</script>