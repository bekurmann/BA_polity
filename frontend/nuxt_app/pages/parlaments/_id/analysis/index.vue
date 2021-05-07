<template>

    <v-container ma-0 mt-3 pa-0>
        <v-row>
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                <AnalysisParlamentAffairsPerYearOW :numberOfAffairsPerYear="numberOfAffairsPerYear"></AnalysisParlamentAffairsPerYearOW>
            </v-col>

            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                <AnalysisParlamentAffairsTypeOW :numberOfAffairsTypes="numberOfAffairsTypes"></AnalysisParlamentAffairsTypeOW>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                <AnalysisParlamentDaysNumberAffairs :MembershipsOW="MembershipsOW"></AnalysisParlamentDaysNumberAffairs>
            </v-col>
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                <AnalysisParlamentTypesPerYear :numberOfAffairsTypesPerYear="numberOfAffairsTypesPerYear"></AnalysisParlamentTypesPerYear>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                <AnalysisParlamentInterpellation :analysisInterpellation="analysisInterpellation"></AnalysisParlamentInterpellation>
            </v-col>
            <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">

            </v-col>
        </v-row>
    </v-container>

</template>
<script>
import AnalysisParlamentAffairsPerYearOW from '~/components/analysis/AnalysisParlamentAffairsPerYearOW.vue'
import AnalysisParlamentAffairsTypeOW from '~/components/analysis/AnalysisParlamentAffairsTypeOW.vue'
import AnalysisParlamentDaysNumberAffairs from '~/components/analysis/AnalysisParlamentDaysNumberAffairs.vue'
import AnalysisParlamentTypesPerYear from '~/components/analysis/AnalysisParlamentTypesPerYear.vue'
import AnalysisParlamentInterpellation from '~/components/analysis/AnalysisParlamentInterpellation.vue'

export default {
    async asyncData({params, $axios}) {
        const numberOfAffairsPerYear = await $axios.$get(`/analysis/ow/affairsperyear/`);
        const numberOfAffairsTypes = await $axios.$get(`/analysis/ow/affairstypes`);
        const MembershipsOW = await $axios.$get(`/parlaments/${params.id}/memberships/`);
        const numberOfAffairsTypesPerYear = await $axios.$get(`/analysis/ow/affairstypesperyear`);
        const analysisInterpellation = await $axios.$get(`/analysis/ow/interpellation`);
        
        return {
            numberOfAffairsPerYear: numberOfAffairsPerYear,
            numberOfAffairsTypes: numberOfAffairsTypes,
            MembershipsOW:  MembershipsOW,
            numberOfAffairsTypesPerYear: numberOfAffairsTypesPerYear,
            analysisInterpellation: analysisInterpellation,
        }
    },
    components: {
        AnalysisParlamentAffairsPerYearOW,
        AnalysisParlamentAffairsTypeOW,
        AnalysisParlamentDaysNumberAffairs,
        AnalysisParlamentTypesPerYear,
        AnalysisParlamentInterpellation,
    },
    middleware: ['auth'],
    layout: 'ParlamentDetail',
}
</script>