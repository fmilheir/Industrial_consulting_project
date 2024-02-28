<template>
    <div>
        <h1>Login</h1>
        <form @submit.prevent="login">
            <div>
                <label for="email">Email</label>
                <input type="text" id="email" v-model="email" required>
            </div>
            <div>
                <label for="password">Password</label>
                <input type="password" id="password" v-model="password" required>
            </div>
            <div><router-link to="/confirmEmail">Forgot Password?</router-link></div>
            <div>
                <button type="submit">Login</button>
            </div>
        </form>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                email: '',
                password: '',
            };
        },
        methods: {
            login() {
                fetch(`${process.env.VUE_APP_BACKEND_URL}/login`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        email: this.email,
                        password: this.password
                    })
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Invalid email or password');
                    }
                    return response.json();
                })
                .then(response => response.json())
                .then(data => {
                    console.log('Success:', data);
                    this.$router.push('/dashboard');
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            }
        }
    };
</script>