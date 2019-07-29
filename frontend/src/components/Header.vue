<template>
    <v-toolbar class="teal title shrink" short>
        <v-toolbar-title class="white--text font-weight-light subtitle-1">Ludovic Ortega</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items v-if="$vuetify.breakpoint.mdAndUp">
            <v-btn
                    v-for="(link, index) in links"
                    v-bind:key="index"
                    text
                    class="white--text font-weight-light subtitle-1"
                    v-bind:to="link.url"
            >{{ link.name }}&nbsp;
                <v-icon size="24px" right>{{ link.icon }}</v-icon>
            </v-btn>
        </v-toolbar-items>
        <v-menu v-if="$vuetify.breakpoint.smAndDown" class="text--white">
            <template v-slot:activator="{ on }">
                <v-btn
                        dark
                        icon
                        v-on="on"
                >
                    <v-icon>fas fa-ellipsis-v</v-icon>
                </v-btn>
            </template>

            <v-list>
                <v-list-item
                        v-for="(link, index) in links"
                        v-bind:key="index"
                >
                    <v-list-item-title>
                        <v-btn
                            class="white--text font-weight-light subheading"
                            v-bind:to="link.url"
                            color="teal"
                            block
                        >
                            {{ link.name }}
                            <v-spacer></v-spacer>
                            <v-icon size="24px" right>{{ link.icon }}</v-icon>
                        </v-btn>
                    </v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>
    </v-toolbar>
</template>

<script>
    export default {
        name: "Header",
        data: () => ({
            links: [
                {name: "About", url: "/About", icon: "fas fa-address-card"},
                {name: "Portfolio", url: "/Portfolio", icon: "fas fa-clipboard-list"},
                {name: "Contact", url: "/Contact", icon: "fas fa-envelope"}
            ]
        })
    };
</script>