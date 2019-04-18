<template>
    <v-footer
            dark
            height="155"
    >
        <v-card
                flat
                tile
                class="teal white--text text-xs-center flex"
        >
            <v-card-text>
                <v-btn
                        v-for="contact in contacts"
                        v-bind:key="contact.id"
                        class="mx-3 white--text"
                        v-bind:href="contact.url"
                        target="_blank"
                        icon
                >
                    <v-icon medium>{{ get_icon(contact.type) }}</v-icon>
                </v-btn>
                 <v-btn
                        class="mx-3 white--text"
                        href="#/contact"
                        icon
                >
                    <v-icon medium>fas fa-envelope</v-icon>
                </v-btn>
            </v-card-text>

            <v-divider></v-divider>

            <v-card-text class="font-weight-light subheading grey darken-3 justify-center">
                &copy;2019 - Ludovic Ortega
            </v-card-text>
        </v-card>
    </v-footer>
</template>

<script>
    import ApiService from '@/store/ApiService'
    import Graphics from '@/store/graphics'
    export default {
        name: "Footer",
        data: () => ({
            person_id: '1',
            contacts: null
        }),
        mounted () {
            this.getSocials(this.person_id)
        },
        methods: {
            async getSocials(id) {
                try {
                    const response = await ApiService.getSocials(id);
                    this.contacts = response.data;
                }
                catch (e) {
                    this.api_error = true;
                }
            },
            get_icon: function(type)
            {
                return Graphics.get_icon(type);
            }
        }
    }
</script>