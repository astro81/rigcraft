// $lib/stores/user-store.svelte.js
export const userDataStore = $state({
    username: '',
    isLoggedIn: false,
});

console.log(userDataStore.username);
