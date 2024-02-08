<template>
    <div>  
        <h1>Hello World</h1>
        <p>{{ message }}</p>
    </div>
</template>
<script>
export default {
    data() {
        return {
            message: ''
        };
    },
    mounted() {
        // make a GET request to the Flash backend
        fetch('/message')
        .then(response => response.json())
        .then(data => {
            this.message = data.message;
        })
        .catch(error => {
            console.error('Error fetching message:', error);
        }); 
    }
};