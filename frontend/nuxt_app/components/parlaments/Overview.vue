<template>
    <v-card class="mt-3">
        <v-card-title>
            General Information
        </v-card-title>
        <v-row>
            <v-col cols="12" xs="12" sm="12" md="3" lg="2" xl="2" class="d-flex child-flex align-stretch">
                <v-card class="mx-3">
                    <v-card-title>Members</v-card-title>
                    <v-card-subtitle>Number of registered members</v-card-subtitle>
                    <v-card-text class="text-h2">{{parlament.number_of_registered_members}}</v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" xs="12" sm="12" md="3" lg="2" xl="2" class="d-flex child-flex align-stretch">
                <v-card class="mx-3">
                    <v-card-title>Fractions</v-card-title>
                    <v-card-subtitle>Number of registered fractions</v-card-subtitle>
                    <v-card-text class="text-h2">{{parlament.number_of_fractions}}</v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" xs="12" sm="12" md="3" lg="2" xl="2" class="d-flex child-flex align-stretch">
                <v-card class="mx-3">
                    <v-card-title>Affairs</v-card-title>
                    <v-card-subtitle>Number of registered affairs</v-card-subtitle>
                    <v-card-text class="text-h2">{{parlament.number_of_affairs}}</v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" xs="12" sm="12" md="3" lg="2" xl="2" class="d-flex child-flex align-stretch">
                <v-card class="mx-3">
                    <v-card-title>Debate</v-card-title>
                    <v-card-subtitle>Number of debate statements</v-card-subtitle>
                    <v-card-text class="text-h2">{{parlament.number_of_debate_statements}}</v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" xs="12" sm="12" md="3" lg="2" xl="2" class="d-flex child-flex align-stretch">
                <v-card class="mx-3">
                    <v-card-title>Sessions</v-card-title>
                    <v-card-subtitle>Number of registered sessions</v-card-subtitle>
                    <v-card-text class="text-h2">{{parlament.number_of_sessions}}</v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" xs="12" sm="12" md="3" lg="2" xl="2" class="d-flex child-flex align-stretch">
                <v-card class="mx-3">
                    <v-card-title>Files</v-card-title>
                    <v-card-subtitle>Number of available files</v-card-subtitle>
                    <v-card-text class="text-h2">{{parlament.number_of_files}}</v-card-text>
                </v-card>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="12" xs="12" sm="12" md="8" lg="8" xl="8">
                <v-card-title>
                    Description
                </v-card-title>
                <v-card-text class="whitespace">
                    <span>{{parlament.description}}</span>
                </v-card-text>
            </v-col>
            <v-col cols="12" xs="12" sm="12" md="4" lg="4" xl="4">
                <v-card-title>
                    Contact
                </v-card-title>
                <v-card-text>

                    {{parlament.title}}<br>
                    {{parlament.street1}} <br>
                    {{parlament.city.plz}} {{parlament.city.name}}<br><br>
                    {{parlament.website}}<br>
                    {{parlament.email}}<br>
                    {{parlament.phone}}<br><br><br>
                    <v-img :src="parlament.avatar" max-width="600" contain></v-img>
                </v-card-text>
            </v-col>
        </v-row>
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