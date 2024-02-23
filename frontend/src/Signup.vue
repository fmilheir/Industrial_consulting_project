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
                <label for="phoneNumber">Telephone  Number (Format: 7xxxxxxxxx)</label><br>
                <input type="tel" name="phoneNumber" id="phoneNumber" pattern="[0-9]{10}" v-model="phoneNumber" required>
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
                .then(response => {
                    if (!response.ok) {
                        //throw new Error(`HTTP error! status: ${response.status}`);
                        return response.json().then(err => {
                            // This will handle JSON response containing the error
                            throw new Error(`Backend error: ${err.message}\nTrace: ${err.traceback}`);
                        });
                        
                    } else {
                        return response.json(); // Only parse if the response is OK.
                    }
                })
                .then(data => {
                    if (data.error) {
                        alert(data.error);
                    } else if  (data.token) {
                        console.log('Verification token:', data.token);
                        console.log("Data being sent:", JSON.stringify({
                        firstName: this.firstName,
                        lastName: this.lastName,
                        email: this.email,
                        phoneNumber: this.phoneNumber,
                        password: this.password
                    }))
                    alert('Signup successful! Redirecting to login...');
                    this.$router.push('/login');
                    } else {
                        alert('An unexpected error occurred.');
                    }
                    
                    
                })
                .catch(error => {
                    console.error('Error during the signup:', error);
                    if (error instanceof Response && error.status === 500) {
                        // If the error is a network response with a 500 status, try to get JSON
                        error.json().then(err => {
                            alert(`Error during signup: ${err.message || "An unexpected server error occurred."}`);
                        }).catch(jsonError => {
                            // The response might not be in JSON format, hence the error
                            alert(`Error during signup: ${error.statusText || "An unexpected error occurred."}`);
                        });
                    } else {
                        // If the error is not a network error, display its message directly
                        alert(`Error during signup: ${error.message}`);
                    }
                });
            }
        }
    }
</script>