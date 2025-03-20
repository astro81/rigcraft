<!-- /users/[user_name]/ -->
<script>
	import { userDataStore } from '$lib/stores/user-store.svelte';

    /** @type {{ data: import('./$types').PageData }} */
    let { data } = $props();

    // Use the userDataStore to fetch and update user data
    let username = userDataStore.username;
    let loginStatus = userDataStore.isLoggedIn;

    // $inspect(username);
    // $inspect(loginStatus);
</script>

<!-- <h1>{data.username}</h1> -->
<h1>{username}</h1>

{#if loginStatus}
    <p class="text-white">You are logged in.</p>
{/if}
