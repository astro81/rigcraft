// $lib/stores/user-store.svelte.js
export const userDataStore = $state({
    username: '',
    isLoggedIn: false,
    token: '', // Add a token field
});

// update the store after login
export function setUserData(username, token) {
    userDataStore.username = username;
    userDataStore.isLoggedIn = true;
    userDataStore.token = token;
}

// clear the store after logout
export function clearUserData() {
    userDataStore.username = '';
    userDataStore.isLoggedIn = false;
    userDataStore.token = '';
}