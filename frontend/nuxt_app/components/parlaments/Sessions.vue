<template>
    <v-card>
        <v-card-title>
            Sessions
        </v-card-title>
        <v-card-text>

            <v-data-iterator
                :items="sessions"
                item-key="id"
                :items-per-page="15"
                :search="search"
                :sort-by="sortBy.toLowerCase()"
                :sort-desc="sortDesc"
            >
                <template v-slot:header>
                    <v-toolbar color="primary" dark>
                        <v-text-field
                            v-model="search"
                            clearable
                            flat
                            solo-inverted
                            hide-details
                            prepend-inner-icon="mdi-magnify"
                            label="Search"
                        ></v-text-field>
                        <template v-if="$vuetify.breakpoint.mdAndUp">
                            <v-spacer></v-spacer>
                            <v-select
                            v-model="sortBy"
                            flat
                            solo-inverted
                            hide-details
                            :items="keys"
                            label="Sort by"
                            ></v-select>
                            <v-spacer></v-spacer>
                            <v-btn-toggle
                            v-model="sortDesc"
                            mandatory
                            >
                            <v-btn
                                large
                                depressed
                                color="blue"
                                :value="false"
                            >
                                <v-icon>mdi-arrow-up</v-icon>
                            </v-btn>
                            <v-btn
                                large
                                depressed
                                color="blue"
                                :value="true"
                            >
                                <v-icon>mdi-arrow-down</v-icon>
                            </v-btn>
                            </v-btn-toggle>
                        </template>
                    </v-toolbar>
                </template>


                <template v-slot:default="{ items }">

                    <v-simple-table>
                            <tbody>
                                <tr v-for="(session) in items" :key="session.id">
                                    <td>
                                        {{session.start_date}}
                                    </td>
                                    <td>
                                        {{session.end_date}}
                                    </td>
                                    <td>
                                        <v-chip v-if="session.opening_session" color="green" dark>opening session</v-chip>
                                        <v-chip v-else color="yellow">regular session</v-chip>
                                    </td>
                                    <td>
                                        <a :href="session.word_protocol">
                                            {{getFileName(session.word_protocol)}}
                                        </a>
                                    </td>
                                </tr>
                            </tbody>
                    </v-simple-table>

                </template>
                
            </v-data-iterator>

        </v-card-text>
    </v-card>
</template>
<script>
export default {
    data() {
        return {
            itemsPerPage: 15,
            search: '',
            sortBy: 'id',
            sortDesc: false,
            keys: [
                'id',
                'start_date',
                'end_date',
                'opening_session',
            ],
        }
    },
    props: {
        sessions: {
            type: Object
        },
    },
    methods: {
        getFileName(filePath) {
            let slicedFilePath = filePath.split("/");
            let [fileName] = slicedFilePath.slice(-1);
            return fileName
        }
    }
}
</script>