<template>
    <div>
        <h1>Sign Up</h1>
        <form @submit.prevent="signup">
            <div>
                <label for="firstName">First Name</label>
                <input type="text" id="firstName" v-model="firstName" required>
            </div>
            <div>
                <label for="lastName">Last Name</label>
                <input type="text" id="lastName" v-model="lastName" required>
            </div>
            <div>
                <label for="email">E-mail</label>
                <input type="email" id="email" v-model="email" required>
            </div>
            <div>
                <label for="phoneNumber">Telephone  Number (Format: 07xx-xxx-xxxx)</label><br>
                <input type="tel" name="phoneNumber" id="phoneNumber" pattern="[0-9]{4}-[0-9]{3}-[0-9]{4}" v-model="phoneNumber" required>
            </div>
            <div>
                <label for="password">Password</label>
                <input type="password" id="password" v-model="password" required>
            </div>
            <div>
                <label for="confirmpassword">Confirm Password</label>
                <input type="password" id="confirmpassword" v-model="confirmPassword" required>
            </div>
            <div>
                <button type="submit">Sign Up</button>
            </div>
        </form>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                firstName:'',
                lastName:'',
                email: '',
                password: '',
                confirmPassword: '',
                phoneNumber:''
            };
        },
        methods: {
            signup() {
                if(this.password !== this.confirmPassword){
                    alert("Passwords do not match");
                    return;
                }
                console.log(process.env.VUE_APP_BACKEND_URL)
                fetch(`${process.env.VUE_APP_BACKEND_URL}/signup`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        firstName: this.firstName,
                        lastName: this.lastName,
                        email: this.email,
                        phoneNumber: this.phoneNumber,
                        password: this.password
                    })
                })
                .then(response => response.json())
                .then(data => {
                    console.log('Success:', data);
                    this.$router.push('/login');
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            }
        }
    }
</script>