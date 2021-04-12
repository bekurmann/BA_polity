<template>
    <v-card>
        <v-card-title primary-title>
            General Information
        </v-card-title>
        <v-card-text class="whitespace">
            <span>{{parlament.description}}</span>
        </v-card-text>
        <v-card-title>
            Contact
        </v-card-title>
        <v-card-text>
            <v-row>
                <v-col cols="12" xs="12" sm="12" md="12" lg="12" xl="12">
                    {{parlament.title}}<br>
                    {{parlament.street1}} <br>
                    {{parlament.city.plz}} {{parlament.city.name}}<br><br>
                    {{parlament.website}}<br>
                    {{parlament.email}}<br>
                    {{parlament.phone}}
                </v-col>
            </v-row>
        </v-card-text>
    </v-card>
</template>
<script>
export default {
    props: {
        parlament: {
            type: Object
        }
    }
}
</script>
<style>
.whitespace {
    white-space: pre-wrap;
}   
</style>