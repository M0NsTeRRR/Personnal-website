<template>
    <v-footer
            dark
            height="145"
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
                    <v-icon medium>{{ getIcon(contact.type) }}</v-icon>
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
    import ApiService from "@/store/ApiService";
    import Graphics from "@/store/graphics";
    export default {
        name: "Footer",
        data: () => ({
            personId: "1",
            contacts: null
        }),
        mounted () {
            this.getSocials(this.personId);
        },
        methods: {
            async getSocials(id) {
                try {
                    const response = await ApiService.getSocials(id);
                    this.contacts = response.data;
                }
                catch (e) {
                    //
                }
            },
            getIcon: function(type)
            {
                return Graphics.getIcon(type);
            }
        }
    };
</script>