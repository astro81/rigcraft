<script>
    import { browser } from '$app/environment';
    import { login } from '$lib/api.js';
	import { preventDefault } from 'svelte/legacy';
	import Input from './Input.svelte';
    
    let { toggleForm } = $props();

    let username = $state('');
    let password = $state('');
    
    let error = $state({});
    
    let isLoading = $state(false);

    const handleLogin = async () => {
        error = {};

        //* Frontend validation for empty fields
        if (!username) error.username = "Username is required.";
        if (!password) error.password = "Password is required.";

        //* Stop the submission if there are errors
        if (Object.keys(error).length > 0) return;

        isLoading = true;

        try {
            const data = await login(username, password);
            
            if (browser) {

                localStorage.setItem('token', data.access_token);
                localStorage.setItem('refreshToken', data.refresh_token); // Store refresh token

                window.location.href = '/users/profile';
            }

        } catch (err) {
            // Handle backend validation errors
            if (err.response?.data?.errors) {
                // Assign the error object from the backend
                error = err.response.data.errors;
            } else {
                error.general = "Login failed. Please try again.";
            }
            console.error('Login error:', err.response?.data);
        } finally {
            isLoading = false;
        }
    };
</script>

<form 
    class="w-full transition-all duration-300" 
    onsubmit={preventDefault(handleLogin)}
    >
    <div class="relative flex flex-col my-5">
        <Input type="text" placeholder="Username" bind:value={username}/>
        <i class='bx bx-envelope absolute top-1/2 right-6 -translate-y-1/2 text-xl text-white'></i>
        {#if error.username}
            <p style="color: red;">{error.username}</p>
        {/if}
    </div>

    <div class="relative flex flex-col my-5">
        <Input type="password" placeholder="Password" bind:value={password}/>
        <i class='bx bx-lock-alt absolute top-1/2 right-6 -translate-y-1/2 text-xl text-white'></i>
        {#if error.password}
            <p style="color: red;">{error.password}</p>
        {/if}
    </div>

    {#if error.general}
        <p style="color: red;">{error.general}</p>
    {/if}

    <div class="relative flex flex-col my-5">
        <button
            type="submit" 
            class="flex items-center justify-center gap-2.5 w-full h-[50px] outline-1 outline-[var(--border-color)] text-white text-base font-medium rounded-3xl cursor-pointer transition-all duration-300 hover:outline-[#E3E4E6]" 
            disabled={isLoading}
        >{isLoading ? 'Logging in...' : 'Login'}
            <i class='bx bx-log-in text-xl'></i>
        </button>
    </div>

    <div class="text-center">
        <span>Don't have an account? 
            <a 
                href="/users/register" class="font-medium text-white transition-all duration-300 hover:underline" 
                onclick={preventDefault(toggleForm)}
                >Register</a>
        </span>
    </div>
</form>