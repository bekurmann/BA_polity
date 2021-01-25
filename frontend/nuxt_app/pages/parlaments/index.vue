<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title primary-title>
                        Parlaments
                    </v-card-title>
                    <v-card-subtitle>Check out already registered parlaments. </v-card-subtitle>
                    <v-card-text>
                        <ParlamentList></ParlamentList>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        
    </v-container>
</template>
<script>
import ParlamentList from '~/components/parlaments/ParlamentList.vue'

export default {
    components: {
        ParlamentList
    },
    middleware: ['auth-user']
}
</script>