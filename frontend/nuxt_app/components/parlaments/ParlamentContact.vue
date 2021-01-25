<template>
    <v-card>
        <v-card-title primary-title>
            Contact
        </v-card-title>
        <v-card-text>
            <v-row>
                <v-col>
                    <v-img :src="parlament.avatar" max-height="200" alt="canton emblem"></v-img>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
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