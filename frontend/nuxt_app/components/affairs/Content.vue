<template>
    <v-card>
        <v-card-title>Content</v-card-title>
        <v-card-text>
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