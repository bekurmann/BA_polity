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
                 <v-form v-model="formValid" @submit.prevent="registerUser"> 
                    <v-text-field label="Username" placeholder="Your Username" outline required v-model="username"></v-text-field>

                    <v-text-field label="Firstname" placeholder="Your Firstname" outline required v-model="firstname"></v-text-field>

                    <v-text-field label="Lastname" placeholder="Your Lastname" outline required v-model="lastname"></v-text-field>
                    

                    <v-text-field label="eMail" placeholder="Your eMail" required v-model="email" :rules="[formRules.required, formRules.validEmail]"></v-text-field>

                    <v-text-field
                    v-model="password1"
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
                    v-model="password2"
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
                    <v-btn block color="red" type="submit" dark>SignUp</v-btn>
                </v-form>
                <v-spacer class="ma-10"></v-spacer>
                <v-divider></v-divider>
                <v-spacer class="ma-10"></v-spacer>
                <p>Already have an account?</p>
                <p><v-btn block color="info" to="/login" dark>Login</v-btn></p>
            </v-card-text>
        
    </v-card>
</v-container>
</template>

<script>

export default {
    data () {
        return {
            formValid: false,

            username: '',
            firstname: '',
            lastname: '',
            email: '',
            password1: '',
            password2: '',
            terms: false,

            pwShow: false,
            formRules: {
                required: value => !!value || 'Required.',
                min: v => v.length >= 8 || 'Min 8 characters',
                //emailMatch: () => ('The email and password you entered don\'t match'),
                validEmail: v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid',
                pwMatch: () => (this.password1 == this.password2) || 'Passwords must match',
            },
        }
    },
    methods: {
        async registerUser () {
            if(this.formValid) {
                try {
                    await this.$axios.$post('/auth/registration/', {
                        first_name: this.firstname,
                        last_name: this.lastname,
                        username: this.username,
                        email: this.email,
                        password1: this.password1,
                        password2: this.password2
                    })
                    this.$router.push('/')
                    this.$notifier.showSnackbar({content: 'Registration successful. Check your e-mail to confirm registration process.', color: 'success'})
                } catch(error) {
                    console.log(error)
                }
            } else {
                this.$notifier.showSnackbar({ content: 'Your inputs are not valid. Try again!', color: 'info' })
            }
        }
    }
}
</script>