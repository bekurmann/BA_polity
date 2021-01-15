<template>
    <v-container>
        <v-row>
            <v-col cols="12"><!--md="12" lg="12" xl="12" -->
                <v-card>
                    <v-card-title primary-title>
                        Where do you want to start?
                    </v-card-title>
                    <v-card-subtitle>select an area.</v-card-subtitle>
                    <v-card-text>
                        <!-- map -->
                        <v-img id="map"></v-img>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        
    </v-container>
</template>
<script>
export default {
    middleware: 'auth'
}
</script>