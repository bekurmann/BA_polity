<template>
    <v-card class="ma-1" light>
        <v-card-title>Affair Files</v-card-title>
        <v-card-text>

            <v-list-item v-for="file in files" :key="file.id">
                <v-list-item-icon v-if="determineFileType(file.affair_file) == 'pdf'">
                    <v-icon color="primary">mdi-file-pdf</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title>{{file.affair_file}}</v-list-item-title>
                </v-list-item-content>
            </v-list-item>

        </v-card-text>
    </v-card>
</template>
<script>
export default {
    data() {
        return {
            files: {},
        }
    },
    async fetch() {
        try {
            const affairFiles = await this.$axios.$get(this.$route.path +'/files/')
            console.log(this.$route.path +'/files/')
            this.files = affairFiles
        } catch(error) {
            throw new Error('Failed to fetch affairFiles from '+ this.$route.path +'/files/')
        }
    },
    methods: {
        determineFileType(filePath) {
            let slicedFilePath = filePath.split(".");
            let [fileType] = slicedFilePath.slice(-1);
            return fileType
        }
    }

}
</script>