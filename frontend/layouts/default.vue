<template>
    <v-app>
        <v-navigation-drawer
                app
                class="primary onprimary--text"
                temporary
                right
                v-model="rightDrawer"
        >
            <header-account :isLoggedIn="!!$store.state.auth.user"></header-account>
            <v-divider></v-divider>

            <v-list>
                <v-list-item
                        v-for="item in items"
                        :key="item.title"
                        @click=""
                        :to="item.to"
                >
                    <v-list-item-content class="primary onprimary--text">
                        <v-list-item-title>{{ item.title }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>

        <v-app-bar app class="primary onprimary--text" :clipped-left="clipped">
            <v-toolbar-title>
                <v-btn text color="onprimary" x-large to="/">{{ title }}</v-btn>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn
                    class="primary onprimary--text"
                    icon
                    @click.stop="rightDrawer = !rightDrawer"
            >
                <v-icon>mdi-menu</v-icon>
            </v-btn>
        </v-app-bar>

        <v-content>
            <nuxt/>
        </v-content>

        <v-footer app>
            <!-- -->
        </v-footer>

    </v-app>
</template>

<script>
    import HeaderAccount from "~/components/HeaderAccount.vue";

    export default {
        components: {
            HeaderAccount
        },
        data() {
            return {
                clipped: false,
                items: [
                    {title: 'Conditions', to: '/conditions'},
                    {title: 'Spells', to: '/spells'},
                    {title: 'Monsters', to: '/monsters'},
                    {title: 'Musics', to: '/musics'}
                ],
                rightDrawer: false,
                title: 'AWM project',
            }
        },
        beforeCreate() {
            if (process.client)
                document
                    .getElementsByTagName('html')[0]
                    .removeAttribute('style')
        }
    }
</script>

<style scoped>
</style>
