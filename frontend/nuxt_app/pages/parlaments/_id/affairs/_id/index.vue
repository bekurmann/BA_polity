<template>
    <v-container ma-0 mt-3 pa-0>
        <v-row>
            <v-col cols="12" xs="12" sm="12" md="12" lg="12" xl="12">
                <AffairInfo :affair="affair" :politican="politican"></AffairInfo>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <AffairFiles></AffairFiles>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <AffairContent :affair="affair"></AffairContent>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <AffairDebate :affair="affair"></AffairDebate>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import AffairInfo from '~/components/affairs/Info.vue'
import AffairFiles from '~/components/affairs/Files.vue'
import AffairContent from '~/components/affairs/Content.vue'
import AffairDebate from '~/components/affairs/Debate.vue'

export default {
    data() {

    },
    async asyncData({params, $axios}) {
        const affair = await $axios.$get(`/affairs/${params.id}`);
        const politican = await $axios.$get(`/politicans/${affair.signatory}`);
        return { 
            affair: affair,
            politican: politican
        }
    },
    components: {
        AffairInfo,
        AffairFiles,
        AffairContent,
        AffairDebate,
    },
    middleware: ['auth'],
    layout: 'ParlamentDetail',
}
</script>