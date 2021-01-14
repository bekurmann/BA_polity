<template>
<v-container>
    <v-card class="mx-auto" max-width="700">

        <v-img
        src="https://images.pexels.com/photos/167708/pexels-photo-167708.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"
        height="200px"
        ></v-img>

        <v-card-title>
        Login
        </v-card-title>

        <v-card-subtitle>
        login & start!
        </v-card-subtitle>
          
            <v-card-text>
                 <v-form v-model="formValid"> 

                    <v-text-field label="Username" placeholder="Your Username" outlined required v-model="username"></v-text-field>

                    <v-text-field label="eMail" placeholder="Your eMail" outlined required v-model="email" :rules="[pwRules.required, pwRules.validEmail]"></v-text-field>

                    <v-text-field label="Password" placeholder="Your Password" outlined required type="password" v-model="password"></v-text-field>
            
                    <v-btn block color="info" @click.stop="loginUser">Login</v-btn>
                </v-form>
                <v-spacer class="ma-5"></v-spacer>
                <v-divider></v-divider>
                <v-spacer class="ma-5"></v-spacer>
                <p>Don't have a Login?</p>
                <p><v-btn block color="red" to="/login/register" dark>Sign Up</v-btn></p>
            </v-card-text>
        

    </v-card>
    <v-snackbar
      v-model="snackbar"
      :timeout="snackbarTimeout"
      bottom color="error"
    >
      {{ snackbarText }}
      <v-btn
        color="error"
        snackbarText
        @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
</v-container>
</template>

<script>

export default {
    data () {
        return {
            formValid: false,

            snackbar: false,
            snackbarText: 'Enter a valid emailaddress!',
            snackbarTimeout: 2000,

            username: '',
            email: '',
            password: '',
            pwRules: {
                required: value => !!value || 'Required.',
                //emailMatch: () => ('The email and password you entered don\'t match'),
                validEmail: v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid',
            }
        }
    },
    methods: {
        loginUser () {
            if(this.formValid) {
                this.$auth.loginWith('local', {
                    data: {
                        username: this.username,
                        password: this.password
                    }
                })
            } else {
                this.snackbar = true;
            }
        }
    },
}
</script>