<template>
    <div class="p-app">
        <div class="login-container d-flex justify-content-center align-items-center">
            <div class="formulaire">
                <h1 class="mb-4">Welcome</h1>
                <form class="form-group" @submit.prevent="logIn">
                    <input 
                        v-model="emailLogin" 
                        placeholder="Email" 
                        type="email" 
                        required
                    />
                    <input 
                        v-model="passwordLogin" 
                        placeholder="Password" 
                        type="password" 
                        required
                        />
                    <button 
                        class="nav-btn" 
                        type="submit"
                        data-cy="login-button"
                    >
                        Log In
                    </button>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import { ActiveUser } from '@/services/user';
import { AuthService } from '@/services/auth';

export default {
    name: 'LoginView',
    data() {
        return {
            emailLogin: '',
            passwordLogin: '',
        }
    },
    mounted() {
        this.redirectAuthenticated();
    },
    methods: {
        redirectAfterLogin() {
            const pathToLoadAfterLogin = localStorage.getItem('pathToLoadAfterLogin');
            localStorage.removeItem('pathToLoadAfterLogin');
            this.$router.replace((!pathToLoadAfterLogin?.includes("login") && pathToLoadAfterLogin) || '/');
        },
        redirectAuthenticated() {
            if (ActiveUser.get()) this.redirectAfterLogin()
        },
        async logIn() {
            const {res} = await AuthService.login({
                email: this.emailLogin,
                password: this.passwordLogin,
            });
            if (res.status !== 200) {
                return alert('Login failed!')
            }
            this.redirectAuthenticated();
        },
    }
}
</script>
<style lang="scss">
.formulaire {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 500px;
    background-color: #006A4E;
    opacity: 80%;
    overflow: hidden;
    padding: 20px;
    color: white;
}

.form-group {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    gap: 1em;
}
.login-container {
    height: 100vh;
}
</style>