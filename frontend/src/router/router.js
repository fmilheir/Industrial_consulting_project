import Vue from 'vue';
import VueRouter from 'vue-router';
import HelloWorld from '../index.vue';
import Login from '../Login.vue';
import Signup from '../Signup.vue';
import ConfirmEmail from '../confirmEmail.vue';
import ConfirmPassword from '../confirmPassword.vue';
import Redirect from '../redirect.vue';


Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'HelloWorld',
        component: HelloWorld
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/signup',
        name: 'Signup',
        component: Signup
    },
    {
        path: '/confirmEmail',
        name: 'confirmEmail',
        component: ConfirmEmail
    },
    {
        path: '/redirect', 
        name: 'redirect',
        component: Redirect
    },
    {
        path: '/confirmPassword/:token',
        name: 'confirmPassword',
        component: ConfirmPassword
    }
];
const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

export default router;