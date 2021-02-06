<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card class="primary" dark height="100%">
                  <!-- start main -->
                  <v-container>

                    <v-row>
                      <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                        <p class="text-h3 mt-15">We help you to participate.</p><br>
                        <p class="text-h5">Explore democracy online.</p>
                        <p><v-btn outlined x-large to="/registration">Sign up now</v-btn></p>
                      </v-col>
                      <v-col cols="12" xs="12" sm="12" md="6" lg="6" xl="6">
                        <v-card light>
                          <v-img></v-img>
                            <v-img src="/home/participate.png" contain max-height="400"></v-img>
                        </v-card>
                      </v-col>
                    </v-row>

                  </v-container>

                </v-card>
            </v-col>
        </v-row>
        
    </v-container>
</template>
<script>
export default {

}
</script>