<script lang="ts">
	import { preventDefault } from 'svelte/legacy';
    import { userDataStore } from '$lib/stores/user-store.svelte';
    import { browser } from '$app/environment';
    import { getProfile, updateProfile, logout,} from '$lib/apis/user-api.js';
	import DeleteProfile from '../DeleteProfile.svelte';
	import Logout from '../Logout.svelte';


    let profile = $state({
        username: '',
        email: '',
        first_name: '',
        last_name: '',
        bio: '',
        profile_picture: null,
    });
    let profilePictureFile = $state(null);

    let error = $state('');
    let successMessage = $state('');
    let fieldErrors = $state({
        username: '',
        email: '',
        deletePassword: '',
    });
    
    let isLoading = $state(false);

    let access_token = $state('');
    let refresh_token = $state('');
    
    // Delete account  state
    let showDeleteModal = $state(false);
    let deletePassword = $state('');
    let deleteError = $state('');

    //* Fetch profile data
    const fetchProfile = async () => {
        isLoading = true;
        error = '';
        successMessage = '';
        
        try {
            profile = await getProfile(access_token);

            userDataStore.username = profile.username;
            userDataStore.isLoggedIn = true;
        } catch (err) {
            error = err.response?.data?.message || 'Failed to fetch profile';
        } finally {
            isLoading = false;
        }
    };

    //* Handle profile picture file selection
    const handleFileChange = (event) => {
        profilePictureFile = event.target.files[0];
    };

    //* Update profile
    const handleUpdateProfile = async (event) => {
        isLoading = true;
        error = '';
        successMessage = '';
        fieldErrors = { username: '', email: '', deletePassword: ''};
        
        try {
            const formData = new FormData();

            formData.append('username', profile.username);
            formData.append('email', profile.email);
            formData.append('first_name', profile.first_name || '');
            formData.append('last_name', profile.last_name || '');
            
            if (profilePictureFile) {
                formData.append('profile_picture', profilePictureFile);
            }
            if (profile.bio) {
                formData.append('bio', profile.bio);
            }

            const updatedProfile = await updateProfile(access_token, formData);
            profile = updatedProfile;
            profilePictureFile = null;

            successMessage = 'Profile updated successfully!';

        } catch (err) {
            if (err.response?.data) {
                const responseData = err.response.data;
                if (responseData.username) {
                    fieldErrors.username = responseData.username[0];
                }
                if (responseData.email) {
                    fieldErrors.email = responseData.email[0];
                }
                error = responseData.message || 'Failed to update profile';
            } else {
                error = 'Failed to update profile';
            }
        } finally {
            isLoading = false;
        }
    };


    const openDeleteModal = () => {
        showDeleteModal = true;
        deletePassword = '';
        deleteError = '';
    };
    

    // Initialize
    if (browser) {
        access_token = localStorage.getItem('access_token');
        refresh_token = localStorage.getItem('refresh_token');

        if (!access_token) {
            window.location.href = '/users/login';
        } else {
            fetchProfile();
        }
    }


</script>

<div class="min-h-screen bg-black text-white py-8 px-4">
    <h1 class="text-3xl font-light text-center mb-8">Profile</h1>
    
    <div class="max-w-2xl mx-auto bg-black border border-zinc-800 rounded-lg p-8">
        {#if profile}
            <form onsubmit={preventDefault(handleUpdateProfile)} class="space-y-6">
                <div class="space-y-6">
                    <!-- Profile Picture -->
                    <div class="flex flex-col items-center space-y-4">
                        {#if profile.profile_picture}
                            <!-- svelte-ignore a11y_img_redundant_alt -->
                            <img
                                src={profile.profile_picture}
                                alt="Profile Picture"
                                class="w-40 h-40 rounded-full object-cover border-2 border-white"
                            />
                        {/if}
                        <label class="block">
                            <input
                                type="file"
                                onchange={handleFileChange}
                                class="block w-full text-sm text-zinc-400 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-zinc-800 file:text-white hover:file:bg-zinc-700"
                            />
                        </label>
                    </div>

                    <!-- Username -->
                    <div>
                        <label for="username" class="block text-sm font-medium text-zinc-400 uppercase tracking-wide mb-2">
                            Username
                        </label>
                        <input
                            type="text"
                            id="username"
                            bind:value={profile.username}
                            class="w-full bg-zinc-900 border border-zinc-700 rounded-lg px-4 py-2 focus:outline-none focus:border-white"
                        />
                        {#if fieldErrors.username}
                            <p class="mt-1 text-red-500 text-sm">{fieldErrors.username}</p>
                        {/if}
                    </div>

                    <!-- Email -->
                    <div>
                        <label for="email" class="block text-sm font-medium text-zinc-400 uppercase tracking-wide mb-2">
                            Email
                        </label>
                        <input
                            type="email"
                            id="email"
                            bind:value={profile.email}
                            class="w-full bg-zinc-900 border border-zinc-700 rounded-lg px-4 py-2 focus:outline-none focus:border-white"
                        />
                        {#if fieldErrors.email}
                            <p class="mt-1 text-red-500 text-sm">{fieldErrors.email}</p>
                        {/if}
                    </div>

                    <!-- Name Fields -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <label for="first_name" class="block text-sm font-medium text-zinc-400 uppercase tracking-wide mb-2">
                                First Name
                            </label>
                            <input
                                type="text"
                                id="first_name"
                                bind:value={profile.first_name}
                                class="w-full bg-zinc-900 border border-zinc-700 rounded-lg px-4 py-2 focus:outline-none focus:border-white"
                            />
                        </div>

                        <div>
                            <label for="last_name" class="block text-sm font-medium text-zinc-400 uppercase tracking-wide mb-2">
                                Last Name
                            </label>
                            <input
                                type="text"
                                id="last_name"
                                bind:value={profile.last_name}
                                class="w-full bg-zinc-900 border border-zinc-700 rounded-lg px-4 py-2 focus:outline-none focus:border-white"
                            />
                        </div>
                    </div>

                    <!-- Bio -->
                    <div>
                        <label for="bio" class="block text-sm font-medium text-zinc-400 uppercase tracking-wide mb-2">
                            Bio
                        </label>
                        <textarea
                            id="bio"
                            bind:value={profile.bio}
                            rows="4"
                            class="w-full bg-zinc-900 border border-zinc-700 rounded-lg px-4 py-2 focus:outline-none focus:border-white"
                        ></textarea>
                    </div>
                </div>

                <!-- Messages -->
                {#if successMessage}
                    <div class="bg-green-900/50 border border-green-500 text-green-400 px-4 py-3 rounded">
                        {successMessage}
                    </div>
                {/if}

                {#if error}
                    <div class="bg-red-900/50 border border-red-500 text-red-400 px-4 py-3 rounded">
                        {error}
                    </div>
                {/if}

                <!-- Action Buttons -->
                <div class="flex flex-col sm:flex-row gap-4">
                    <button
                        type="submit"
                        class="flex-1 bg-white text-black px-6 py-3 rounded-lg font-medium hover:bg-zinc-200 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                        disabled={isLoading}
                    >
                        {isLoading ? 'Updating...' : 'Update Profile'}
                    </button>
                    
                    <Logout {access_token} {refresh_token}/>
                    
                    <button
                        type="button"
                        onclick={openDeleteModal}
                        class="flex-1 bg-transparent border border-red-500 text-red-500 px-6 py-3 rounded-lg font-medium hover:bg-red-500 hover:text-white transition-colors"
                    >
                        Delete Account
                    </button>
                    
                </div>
            </form>
        {:else}
            <div class="text-center py-8">
                <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-white mx-auto"></div>
                <p class="mt-4 text-zinc-400">Loading profile...</p>
            </div>
        {/if}
    </div>
</div>

<DeleteProfile {showDeleteModal} {deletePassword} {deleteError} {access_token}/>

