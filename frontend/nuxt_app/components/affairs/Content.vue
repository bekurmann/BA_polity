<template>
    <v-card>
        <v-card-title>Content</v-card-title>
        <v-card-text class="whitespace">
            {{affair.content_all}}
        </v-card-text>

    </v-card>
</template>
<script>
export default {
    props: {
        affair: {
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