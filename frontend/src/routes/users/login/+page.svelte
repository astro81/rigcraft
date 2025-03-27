<script>
    import { browser } from '$app/environment';
    import { login } from '$lib/apis/user-api.js';
	import { preventDefault } from 'svelte/legacy';
	import Input from '../Input.svelte';
    
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

                localStorage.setItem('access_token', data.access_token);
                localStorage.setItem('refresh_token', data.refresh_token);

                window.location.href = `/users/profile/${username}`;
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

<section class="size-full">
    <div class="h-screen w-screen flex justify-center items-center">
        <form 
            class="outline-1 outline-[var(--border-color)] rounded-3xl p-8" 
            onsubmit={preventDefault(handleLogin)}
            >
            <div class="relative flex flex-col my-5">
                <Input type="text" placeholder="Username" bind:value={username}/>
                {#if error.username}
                    <p style="color: red;">{error.username}</p>
                {/if}
            </div>

            <div class="relative flex flex-col my-5">
                <Input type="password" placeholder="Password" bind:value={password}/>
                {#if error.password}
                    <p style="color: red;">{error.password}</p>
                {/if}
            </div>

            {#if error.general}
                <p style="color: red;">{error.general}</p>
            {/if}

            <div class="relative flex flex-col my-10">
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
                        >Register</a>
                </span>
            </div>
        </form>
    </div>
</section>

