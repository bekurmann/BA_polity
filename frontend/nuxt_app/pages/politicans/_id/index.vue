<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title primary-title>
                        Politican
                    </v-card-title>
                    <v-card-subtitle>Check out already registered parlaments. </v-card-subtitle>
                    <v-card-text>
                        <Detail></Detail>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        
    </v-container>
</template>
<script>
import Detail from '~/components/politicans/Detail.vue'

export default {
    components: {
        Detail
    },
    middleware: ['auth'],
}
</script>