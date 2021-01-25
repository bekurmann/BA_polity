<template>
    <v-card>
        <v-card-title primary-title>
            General Information
        </v-card-title>
        <v-card-text class="whitespace">
            <span>{{parlament.description}}</span>
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