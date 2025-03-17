<script>
	import { goto } from "$app/navigation";
	import { userDataStore } from "$lib/stores/user-store.svelte.js";
	import { preventDefault } from "svelte/legacy";

	let username = $state('');
	let password = $state('');
	let errors = $state({});

	let handleSubmit = async () => {
		const endpoint = 'http://127.0.0.1:8000/user/login/'; // Django login endpoint
		const requestOptions = {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ username: username, password: password }),
		};

		try {
			const response = await fetch(endpoint, requestOptions);
			const data = await response.json();

			if (response.status === 200) {
				// Save tokens to localStorage (or cookies)
				localStorage.setItem('access_token', data.access);
				localStorage.setItem('refresh_token', data.refresh);

				// Redirect to a protected page
				// goto(`/users/${username}`);
				userDataStore.username = username; // Update user data store
				userDataStore.isLoggedIn = true;
				goto(`/users/${userDataStore.username}`);
			} else {
				errors = data; // Display errors from the backend
				console.log('Error:', errors);
			}
		} catch (error) {
			console.error('Fetch error:', error);
		}
	};
</script>

<section class="w-screen h-screen flex justify-center items-center">
	<div class="outline-1 flex flex-col justify-center items-center p-4">
		<h1 class="text-2xl font-medium">Login</h1>

		<form
			class="flex flex-col justify-center items-center gap-4 m-4"
			onsubmit={preventDefault(handleSubmit)}
		>
			<div class="outline-1">
				<input type="text" placeholder="username" bind:value={username} />
				{#if errors && errors.username}
					<p class="text-red-500">{errors.username[0]}</p>
				{/if}
			</div>
			<div class="outline-1">
				<input type="password" placeholder="password" bind:value={password} />
				{#if errors && errors.password}
					<p class="text-red-500">{errors.password[0]}</p>
				{/if}
			</div>

			<button type="submit" class="outline-1 rounded-[4px] px-3 py-1">Login</button>
		</form>

		<p class="mt-4">
			Don't have an account? <a href="/user/register" class="text-blue-500">Register here</a>.
		</p>
	</div>
</section>