<script>
    import { browser } from '$app/environment';
    import { register } from '$lib/apis/user-api.js';
    import { preventDefault } from 'svelte/legacy';

    import Input from '../Input.svelte';
    
    let username = $state('');
    let email = $state('');
    let password = $state('');
    let first_name = $state('');
    let last_name = $state('');

    let error = $state({}); 
    let isLoading = $state(false);

    const handleRegister = async () => {
        error = {};

        // Frontend validation for empty fields
        if (!username) error.username = "Username is required.";
        if (!email) error.email = "Email is required.";
        if (!password) error.password = "Password is required.";

        // Stop the submission if there are any errors
        if (Object.keys(error).length > 0) return;

        isLoading = true;

        try {
            const userData = {
                username,
                email,
                password,
                first_name,
                last_name,
            };

            const data = await register(userData);
            
            if (browser) {
                window.location.href = '/users/login';
            }

        } catch (err) {
            //* Handle backend validation errors
            if (err.response?.data) {
                error = err.response.data; // Assign the error object from the backend
            } else {
                error.general = "Registration failed. Please try again.";
            }
            console.error('Registration error:', err.response?.data);
        } finally {
            isLoading = false;
        }
    };
</script>

<section class="size-full">
    <div class="h-screen w-screen flex justify-center items-center">
        <form 
            class="outline-1 outline-[var(--border-color)] rounded-3xl p-8"
            onsubmit={preventDefault(handleRegister)}
            >

            <div class="relative flex flex-col my-5">
                <Input type="text" placeholder="Username" bind:value={username}/>
                {#if error.username}
                    <p style="color: red;">{error.username}</p>
                {/if}
            </div>
        
            <div class="relative flex flex-col my-5">
                <Input type="email" placeholder="Email" bind:value={email}/>
                {#if error.email}
                    <p style="color: red;">{error.email}</p>
                {/if}
            </div>
        
            <div class="relative flex flex-col my-5">
                <Input type="password" placeholder="Password" bind:value={password}/>
                {#if error.password}
                    <p style="color: red;">{error.password}</p>
                {/if}
            </div>
        
            <div class="relative flex flex-col my-5">
                <Input type="text" placeholder="First Name" bind:value={first_name}/>
            </div>
        
            <div class="relative flex flex-col my-5">
                <Input type="text" placeholder="Last Name" bind:value={last_name}/>
            </div>
        
            {#if error.general}
                <p style="color: red;">{error.general}</p>
            {/if}
        
            <div class="relative flex flex-col my-10">
                <button
                    type="submit" 
                    class="flex items-center justify-center gap-2.5 w-full h-[50px] outline-1 outline-[var(--border-color)] text-white text-base font-medium rounded-[30px] cursor-pointer transition-all duration-300"  
                    disabled={isLoading}
                >{isLoading ? 'Registering...' : 'Register'}
                    <i class='bx bx-user-plus text-xl'></i>
                </button>
            </div>
        
            <div class="text-center">
                <span>Already have an account? <a href="/users/login" class="font-medium text-white transition-all duration-300 hover:underline">Login</a></span>
            </div>
        </form>
    </div>
</section>