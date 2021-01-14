<template>
<v-container>
    <v-card class="mx-auto" max-width="700">

        <v-img
        src="https://images.pexels.com/photos/3753793/pexels-photo-3753793.jpeg?cs=srgb&dl=people-on-snow-covered-mountain-3753793.jpg&fm=jpg"
        height="200px"
        >
            <template v-slot:placeholder>
                <v-row
                class="fill-height ma-0"
                align="center"
                justify="center"
                >
                <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                </v-row>
            </template>
        </v-img>

        <v-card-title>
        SignUp
        </v-card-title>

        <v-card-subtitle>
        create your account and start engaging!
        </v-card-subtitle>
          
            <v-card-text>
                 <v-form v-model="formValid"> 
                    <v-text-field label="Firstname" placeholder="Your Firstname" outline required v-model="firstname"></v-text-field>

                    <v-text-field label="Lastname" placeholder="Your Lastname" outline required v-model="lastname"></v-text-field>
                    

                    <v-text-field label="eMail" placeholder="Your eMail" required v-model="email" :rules="[formRules.required, formRules.validEmail]"></v-text-field>

                    <v-text-field
                    v-model="password"
                    :append-icon="pwShow ? 'mdi-eye' : 'mdi-eye-off'"
                    :rules="[formRules.required, formRules.min]"
                    :type="pwShow ? 'text' : 'password'"
                    name="input-10-1"
                    label="Your Password"
                    hint="At least 8 characters"
                    counter
                    @click:append="pwShow = !pwShow"
                    ></v-text-field>

                    <v-text-field
                    v-model="rePassword"
                    :append-icon="pwShow ? 'mdi-eye' : 'mdi-eye-off'"
                    :rules="[formRules.required, formRules.min, formRules.pwMatch]"
                    :type="pwShow ? 'text' : 'password'"
                    name="input-10-1"
                    label="Your Password"
                    hint="At least 8 characters"
                    counter
                    @click:append="pwShow = !pwShow"
                    ></v-text-field>

                    <v-checkbox label="Accept terms of service" required v-model="terms" :rules="[formRules.required]"></v-checkbox>
                    <v-btn block color="red" @click.stop="registerUser" dark>SignUp</v-btn>
                </v-form>
                <v-spacer class="ma-10"></v-spacer>
                <v-divider></v-divider>
                <v-spacer class="ma-10"></v-spacer>
                <p>Already have an account?</p>
                <p><v-btn block color="info" to="/login" dark>Login</v-btn></p>
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
            snackbarText: 'Check your Input!',
            snackbarTimeout: 2000,

            firstname: '',
            lastname: '',
            email: '',
            password: '',
            rePassword: '',
            terms: false,

            pwShow: false,
            formRules: {
                required: value => !!value || 'Required.',
                min: v => v.length >= 8 || 'Min 8 characters',
                //emailMatch: () => ('The email and password you entered don\'t match'),
                validEmail: v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid',
                pwMatch: () => (this.password == this.rePassword) || 'Passwords must match',
            },
        }
    },
    methods: {
        registerUser () {
            if(this.formValid) {
                instance.post('/users/', { email: this.email, password: this.password, first_name: this.firstname, last_name: this.lastname })
                .then(res => {
                    console.log(res);
                    if(res.status === 201) {
                        console.log('redirecting');
                        router.replace('/login');
                    } else {
                        console.log('something didnt work');
                    }
                })
                .catch(error => console.log(error));
            } else {
                this.snackbar = true;
            }
        }
    }
}
</script>