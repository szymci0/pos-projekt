<template>
    <div class="p-app">
        <div class="d-flex justify-content-center align-items-center h-100">
            <div class="formulaire">
                <h1 class="mb-4">Welcome</h1>
                <form class="form-group">
                    <input v-model="emailLogin" placeholder="Email" type="email" required />
                    <input v-model="passwordLogin" placeholder="Password" type="password" required />
                    <button class="nav-btn" type="submit" @click="logIn">
                        Log In
                    </button>
                </form>
                or
                <button class="nav-btn" type="submit" @click="signUp">
                    Sign Up
                </button>
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
        signUp() {
            return alert('TOBEDONE');
        }
    }
}
</script>
<style lang="scss">
.formulaire {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #F4D03F;
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
</style>