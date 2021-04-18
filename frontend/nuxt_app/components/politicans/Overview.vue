<template>
    <v-card>
        <v-card-title primary-title>
            {{politicanDetails.first_name}} {{politicanDetails.last_name}}
        </v-card-title>
        <v-card-text>
            <v-row class="mt-3">
                <v-col cols="12" xs="12" sm="12" md="6" lg="4" xl="4">
                    <v-avatar
                        size="150"
                    >
                        <v-img :src="politicanDetails.avatar"></v-img>
                    </v-avatar>
                </v-col>
                <v-col cols="12" xs="12" sm="12" md="6" lg="8" xl="8">
                    {{politicanDetails.city.name}}
                    <span v-if="politicanDetails.gender=='M'"><v-icon>mdi-gender-male</v-icon></span>
                    <span v-else-if="politicanDetails.gender=='F'"><v-icon>mdi-gender-female</v-icon></span>
                    <span v-else><v-icon>mdi-gender-non-binary</v-icon></span>
                    <br>
                    <b v-if="politicanDetails.fractions[0]">{{politicanDetails.fractions[0].name}}</b>
                    <br>
                    {{politicanDetails.title}}<br>
                    {{politicanDetails.profession}}<br>
                    {{politicanDetails.date_of_birth}}
                </v-col>
            </v-row>

            <v-row class="mt-3">
                <v-col cols="12" xs="12" sm="12" md="6" lg="4" xl="4" class="d-flex child-flex align-stretch">
                    <v-card color="primary" dark>
                        <v-card-title>Affairs</v-card-title>
                        <v-card-subtitle>Number of affairs</v-card-subtitle>
                        <v-card-text class="text-h4">{{politicanDetails.number_of_submitted_affairs}}</v-card-text>
                    </v-card>
                </v-col>
                <v-col cols="12" xs="12" sm="12" md="6" lg="4" xl="4" class="d-flex child-flex align-stretch">
                    <v-card color="primary" dark>
                        <v-card-title>Success</v-card-title>
                        <v-card-subtitle>Number of successful affairs</v-card-subtitle>
                        <v-card-text class="text-h4">{{politicanDetails.number_of_successful_affairs}}</v-card-text>
                    </v-card>
                </v-col>
                <v-col cols="12" xs="12" sm="12" md="6" lg="4" xl="4" class="d-flex child-flex align-stretch">
                    <v-card color="primary" dark>
                        <v-card-title>Debate</v-card-title>
                        <v-card-subtitle>Number of statements</v-card-subtitle>
                        <v-card-text class="text-h4">{{politicanDetails.number_of_debate_statements}}</v-card-text>
                    </v-card>
                </v-col>
            </v-row>

        </v-card-text>

        <v-card-actions class="ma-3">
            <v-btn outlined large color="primary" to="/support/">
                <v-icon>mdi-account-check-outline</v-icon>
                Follow
            </v-btn>
            <!-- <v-btn outlined large color="primary" to="/support/">
                <v-icon>mdi-star-plus-outline</v-icon>
                Rate
            </v-btn>
            <v-btn outlined large color="primary" to="/support/">
                <v-icon>mdi-comment-outline</v-icon>
                Comment
            </v-btn> -->
        </v-card-actions>

    </v-card>
</template>
<script>
export default {
    props: {
        politicanDetails: {
            type: Object
        }
    },
}
</script>