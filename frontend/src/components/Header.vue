<template>
    <v-toolbar
            class="teal title"
    >
        <v-spacer></v-spacer>
        <v-toolbar-items
            class="hidden-sm-and-down"
        >
            <v-btn
                    v-for="(link, index) in links"
                    v-bind:key="index"
                    flat
                    class="white--text font-weight-light subheading"
                    v-bind:to="link.url"
            >{{ link.name }}
                <v-icon medium right>{{ link.icon }}</v-icon>
            </v-btn>
        </v-toolbar-items>
        <v-menu class="hidden-md-and-up text--white">
            <v-toolbar-side-icon slot="activator"><v-icon medium color="white">fas fa-ellipsis-v</v-icon></v-toolbar-side-icon>
            <v-list>
                <v-list-tile
                        v-for="(link, index) in links"
                        v-bind:key="index"
                >
                    <v-list-tile-content>
                        <v-btn
                            class="white--text font-weight-light subheading"
                            v-bind:to="link.url"
                            color="teal"
                            block
                        >
                            {{ link.name }}
                            <v-spacer></v-spacer>
                            <v-icon medium right>{{ link.icon }}</v-icon>
                        </v-btn>
                    </v-list-tile-content>
                </v-list-tile>
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