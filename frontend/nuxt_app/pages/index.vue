<template>
  <v-container>
    <!-- generate gradients: https://cssgradient.io/ / colors: https://coolors.co -->
    <v-card class="pa-10" style="background-image: radial-gradient(circle, rgba(0,91,173,1) 1%, rgba(68,142,208,1) 100%)" dark>
      <p class="text-h5">Welcome to polity</p>
      <p class="text-h2">We help you to participate.</p><br>
      <p class="text-h4">Explore your democracy online.</p>
      <p><v-btn outlined x-large to="/registration">Sign up now</v-btn></p>
    </v-card>

    <v-card class="mt-3">
      <v-card-title>Features</v-card-title>
      <v-card-text>

        <v-row>
          <v-col>
            <v-card class="ma-3 mb-15" color="primary" style="background-image: radial-gradient(circle, rgba(0,91,173,1) 1%, rgba(68,142,208,1) 100%)" dark>
              <v-row>
                <v-col cols="12" xs="12" sm="12" md="8" lg="8" xl="8">
                  <v-card-title class="text-h3">Information</v-card-title>
                  <v-card-text>
                    <p class="text-h5">
                      inform yourself via polity.<br>
                      polity lets you find the information you need. Browse politicans, affairs and sessions all in one place.
                    </p>
                  </v-card-text>
                </v-col>
                <v-col cols="12" xs="12" sm="12" md="4" lg="4" xl="4">
                  <v-card class="mt-n10 ml-n5 mb-3">
                    <v-img src="/home/information.png" contain></v-img>
                  </v-card>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
        </v-row>

        <v-row>
          <v-col>
            <v-card class="ma-3 mb-15">
              <v-row>
                <v-col cols="12" xs="12" sm="12" md="8" lg="8" xl="8">
                  <v-card-title class="text-h3">Subscribe</v-card-title>
                  <v-card-text>
                    <p class="text-h5">
                      follow the people you're interested in.<br>
                      with polity, you're always up to date on the activities of the politicans you're most interested in. We notify you, whenever your favourite politicans did something.
                    </p>                    
                  </v-card-text>
                </v-col>
                <v-col cols="12" xs="12" sm="12" md="4" lg="4" xl="4">
                  <v-card class="mt-n10 ml-n5 mb-3">
                    <v-img src="/home/subscribe.png" contain></v-img>
                  </v-card>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
        </v-row>

        <v-row>
          <v-col>
            <v-card class="ma-3 mb-15" color="primary" style="background-image: radial-gradient(circle, rgba(0,91,173,1) 1%, rgba(68,142,208,1) 100%)" dark>
              <v-row>
                <v-col cols="12" xs="12" sm="12" md="8" lg="8" xl="8">
                  <v-card-title class="text-h3">Interaction</v-card-title>
                  <v-card-text>
                    <p class="text-h5">
                      inform yourself via polity.<br>
                      polity lets you find the information you need. Browse politicans, affairs and sessions all in one place.
                    </p>
                  </v-card-text>
                </v-col>
                <v-col cols="12" xs="12" sm="12" md="4" lg="4" xl="4">
                  <v-card class="mt-n10 ml-n5 mb-3">
                    <v-img src="/home/interaction.png" contain></v-img>
                  </v-card>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
        </v-row>

        <v-row>
          <v-col>
            <v-card class="ma-3 mb-15">
              <v-row>
                <v-col cols="12" xs="12" sm="12" md="8" lg="8" xl="8">
                  <v-card-title class="text-h3">Analysis and GeoData</v-card-title>
                  <v-card-text>
                    <p class="text-h5">
                      Find out more about your democracy and check out beautifully designed visualizations and analysis.<br>
                      Furthermore, polity let's you find politicans near you - or just find them on a map.
                    </p>                    
                  </v-card-text>
                </v-col>
                <v-col cols="12" xs="12" sm="12" md="4" lg="4" xl="4">
                  <v-card class="mt-n10 ml-n5 mb-3">
                    <v-img src="/home/analysis.png" contain></v-img>
                  </v-card>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
        </v-row>

      </v-card-text>
    </v-card>
        
  </v-container>
</template>
<script>
export default {

}
</script>