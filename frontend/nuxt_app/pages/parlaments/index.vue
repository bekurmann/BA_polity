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
                        <client-only>
                        <List></List>
                        </client-only>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        
    </v-container>
</template>
<script>
import List from '~/components/parlaments/List.vue'

export default {
    components: {
        List
    },
    middleware: ['auth'],
}
</script>