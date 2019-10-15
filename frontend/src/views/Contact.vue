<template>
    <v-container>
        <br>
        <h1 class="font-weight-thin display-3 text-center animated bounceInDown">Contact</h1>
        <br><br><br>
        <v-layout row wrap>
            <v-flex offset-lg2 lg8 offset-md1 md10 xs12>
                <v-snackbar
                        v-model="message_alert.show"
                        v-bind:timeout="10000"
                        v-bind:top="true"
                        v-bind:color="message_alert.success ? 'success' : 'error'"
                        v-bind:multi-line="true"
                >
                    {{ message_alert.message }}
                    <v-btn
                            text
                            @click="message_alert.show = false"
                    >
                        <v-icon>fas fa-times</v-icon>
                    </v-btn>
                </v-snackbar>
                <v-form
                        ref="form"
                        v-model="valid"
                        lazy-validation
                >
                    <v-layout
                            row
                            v-for="(field, index) in fields"
                            v-bind:key="index"
                    >
                        <component
                                v-bind:is="field.type"
                                class="title animated fadeIn slow"
                                outlined
                                clearable
                                clear-icon="fas fa-times-circle"
                                v-bind:append-outer-icon="field.icon"
                                background-color="teal"
                                color="teal"
                                v-model="$data[field.name]"
                                v-bind:label="field.label"
                                v-bind:rules="$data[field.rules]"
                                required
                        ></component>
                    </v-layout>
                    <v-layout row justify-center>
                        <vue-recaptcha
                                v-model="reCaptcha.checked"
                                ref="recaptcha"
                                sitekey="6Lemqb0UAAAAAA5DNX5uE0ODChbnW0LaetbswUl9"
                                @verify="onCaptchaVerified"
                                @expired="onCaptchaExpired"
                                rules="captchaRules"
                                :loadRecaptchaScript="true"
                        ></vue-recaptcha>
                    </v-layout>
                    <br>

                    <v-layout row justify-center>
                        <v-btn
                                color="teal"
                                class="font-weight-light title white--text animated bounceInUp"
                                v-bind:disabled="!valid"
                                v-bind:loading="loading"
                                @click="validate"
                        >
                            Submit&nbsp;&nbsp;
                            <v-icon size="24px" right>fas fa-paper-plane</v-icon>&nbsp;
                        </v-btn>
                    </v-layout>
                </v-form>
            </v-flex>
        </v-layout>
        <br>
    </v-container>
</template>

<script>
    import { VTextField, VTextarea } from "vuetify/lib";
    import VueRecaptcha from 'vue-recaptcha';
    import ApiService from "@/store/ApiService";

    export default {
        name: "Contact",
        components: { VTextField, VTextarea, VueRecaptcha },
        data: () => ({
            valid : true,
            loading: false,
            message_alert: {
                show: false,
                success: true,
                message: "No message"
            },
            reCaptcha: {
                checked: false,
                token: ""
            },
            name: "",
            nameRules: [
                (v) => !!v || "Name is required",
                (v) => /^.{1,50}$/.test(v) || "Name must be valid (1-50 characters)"
            ],
            subject: "",
            subjectRules: [
                (v) => !!v || "Subject is required",
                (v) => /^.{1,50}$/.test(v) || "Subject must be valid (1-50 character)"
            ],
            email: "",
            emailRules: [
                (v) => !!v || "Email is required",
                (v) => /^([a-zA-Z0-9_.\-+])+@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(v) || "Email must be valid"
            ],
            message: "",
            messageRules: [
                (v) => !!v || "Message is required",
                (v) => /^.{1,2000}$/m.test(v) || "Message must be valid (1-2000 characters)"
            ],
            fields: [
                {icon: "fas fa-user", name: "name", label: "Name", type: "v-text-field", animation: "animated bounceInLeft", rules: "nameRules"},
                {icon: "fas fa-at", name: "email", label: "Email", type: "v-text-field", animation: "animated bounceInRight", rules: "emailRules"},
                {icon: "fas fa-heading", name: "subject", label: "Subject", type: "v-text-field", animation: "animated bounceInLeft", rules: "subjectRules"},
                {icon: "far fa-comment-dots", name: "message", label: "Message", type: "v-textarea", animation: "animated bounceInRight", rules: "messageRules"},
            ]
        }),
        methods: {
            onCaptchaExpired: function () {
                this.reCaptcha.checked = false;
                this.$refs.recaptcha.reset();
            },
            onCaptchaVerified(token) {
                this.reCaptcha.checked = true;
                this.reCaptcha.token = token;
            },
            validate () {
                if (this.$refs.form.validate() && this.reCaptcha.checked) {
                    this.loading = true;
                    this.postMail(this.name, this.email, this.subject, this.message, this.reCaptcha.token);
                } else if(this.reCaptcha.checked === false) {
                    this.message_alert.success = false;
                    this.message_alert.message = "reCaptcha must be checked";
                    this.message_alert.show = true;
                }
            },
            async postMail(name, email, subject, message, reCaptchaToken) {
                try {
                    const response = await ApiService.postMail(name, email, subject, message, reCaptchaToken);
                    this.message_alert.success = response.data.success;
                    this.message_alert.message = response.data.message;
                    this.message_alert.show = true;
                    this.loading = false;
                    if(this.message_alert.success === true)
                    {
                        this.$refs.form.reset();
                        this.onCaptchaExpired();
                    }
                }
                catch (e) {
                    this.loading = false;
                    this.message_alert.success = false;
                    this.message_alert.message = "Something wrent wrong. Sorry for inconveniance, try again later.";
                    this.message_alert.show = true;
                    this.onCaptchaExpired();
                }
            }
        }
    };
</script>
