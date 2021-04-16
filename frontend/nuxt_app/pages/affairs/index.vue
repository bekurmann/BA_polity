<template>

    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title primary-title>
                        Affairs
                    </v-card-title>
                    <v-card-subtitle>Check out already registered affairs. </v-card-subtitle>
                    <v-card-text>
                        List view Affairs (all parlaments?) -> newest first?
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        
    </v-container>
</template>
<script>
export default {
    middleware: ['auth'],
}
</script>