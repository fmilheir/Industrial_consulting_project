<template>
    <div>
        <h1>Set New Password</h1>
        <form @submit.prevent="confirmPasswordReset">
            <div>
                <label for="password">New Password</label>
                <input type="password" id="password" v-model="password" required>
            </div>
            <div>
                <label for="confirmPassword">Confirm New Password</label>
                <input type="password" id="confirmPassword" v-model="confirmPassword" required>
            </div>
            <div>
                <button type="submit" :disabled="!passwordsMatch">Reset Password</button>
                <span v-if="!passwordsMatch">Passwords do not match</span>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            password: '',
            confirmPassword: '', 
            resetToken: ''
        };
    },
    mounted() {
        // Extract the reset token from the URL
        this.resetToken = this.$route.params.token;
    },
    computed : {
        passwordsMatch() {
            return this.password && this.password === this.confirmPassword;
        }
    },
    methods: {
        confirmPasswordReset() {
            // Hash the password on the client-side before send ing it to the backend
            const password = this.password;

            // Call the backedend endpoint to coinfirm the password reset
            fetch(`${process.env.VUE_APP_BACKEND_URL}/confirm_password_reset`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    email: this.email,
                    resetToken: this.resetToken,
                    password: this.password

                }),
            })
            .then(response => {
                console.log('Backend response:', response);
                return response.json()
            })
            .then(data => {
                if (response.ok) {
                    // Successful response (status 200)
                    alert('Password reset successfully');
                    this.$router.push('/login');
                } else {
                    // Error response
                    console.error('Data from backend:', data);
                    alert('An error occurred while processing your request.');
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }
    }
};
</script>
