<template>
  <v-app>
    <!-- navigation drawer ********************************** -->
    <v-navigation-drawer
      v-model="drawer"
      clipped
      fixed
      app
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- app bar ********************************** -->
    <v-app-bar
      clipped-left
      fixed
      color="white"
      app
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-img src="/polity_small.png" class="mx-2" max-height="40" max-width="40" contain />
      <v-toolbar-title v-text="title" />
      <v-spacer />
      
      <div v-if="$auth.loggedIn">
        <v-avatar
          size="avatarSize"
          color="red"
        >
          <v-img :src="$auth.user.avatar" class="mx-2" max-height="40" max-width="40" contain v-if="$auth.user.avatar != null" />
          <v-img src="/avatar.png" class="mx-2" max-height="40" max-width="40" contain v-else />
        </v-avatar>
        <v-btn color="success" @click="$auth.logout()">Logout</v-btn>
        
      </div>
      <div v-else>
        <v-btn outlined to="/login">Login</v-btn>
      </div>
      

    </v-app-bar>

    <!-- main ********************************** -->
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>

    <!-- global Snackbar -->
    <Snackbar></Snackbar>

  </v-app>
</template>

<script>
import Snackbar from '~/components/Snackbar.vue'

export default { 
  components: {
    Snackbar
  },
  data () {
    return {
      title: 'polity',
      drawer: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/'
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Inspire',
          to: '/inspire'
        }
      ],
    }
  }
}
</script>
