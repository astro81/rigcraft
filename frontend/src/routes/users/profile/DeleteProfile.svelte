<script>
	import { deleteAccount } from '$lib/apis/user-api.js';

    let { showDeleteModal, deletePassword = $bindable(), deleteError, access_token } = $props();

    // let access_token = $state('');
    // let refreshToken = $state('');

    let isDeleting = $state(false);

    // Delete account modal state
    // let showDeleteModal = $state(false);
    // let deletePassword = $state('');
    // let deleteError = $state('');

    // const openDeleteModal = () => {
    //     showDeleteModal = true;
    //     deletePassword = '';
    //     deleteError = '';
    // };
    
    const closeDeleteModal = () => {
        showDeleteModal = false;
        deletePassword = '';
        deleteError = '';
    };
    
    const handleDeleteAccount = async () => {
        if (!deletePassword) {
            deleteError = 'Password is required';
            return;
        }
        
        isDeleting = true;
        deleteError = '';
        
        try {
            await deleteAccount(access_token, deletePassword);

            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            
            window.location.href = '/users/login?deleted=true';
        } catch (err) {
            if (err.response?.data?.errors?.password) {
                deleteError = err.response.data.errors.password;
            } else {
                deleteError = err.response?.data?.message || 'Failed to delete account';
            }
        } finally {
            isDeleting = false;
        }
    };

</script>

{#if showDeleteModal}
    <div class="fixed inset-0 bg-black/75 flex items-center justify-center p-4 z-50">
        <div class="bg-zinc-900 rounded-lg p-6 max-w-md w-full">
            <h2 class="text-xl font-semibold mb-4">Delete Account</h2>
            <p class="text-zinc-400 mb-4">This action cannot be undone. All your data will be permanently deleted.</p>
            
            <div class="mb-4">
                <label for="delete-password" class="block text-sm font-medium text-zinc-400 uppercase tracking-wide mb-2">
                    Password
                </label>
                <input 
                    type="password" 
                    id="delete-password" 
                    bind:value={deletePassword}
                    placeholder="Enter your password"
                    class="w-full bg-zinc-800 border border-zinc-700 rounded-lg px-4 py-2 focus:outline-none focus:border-white"
                />
                {#if deleteError}
                    <p class="mt-1 text-red-500 text-sm">{deleteError}</p>
                {/if}
            </div>
            
            <div class="flex gap-4">
                <button 
                    class="flex-1 bg-zinc-800 text-white px-4 py-2 rounded-lg hover:bg-zinc-700 transition-colors"
                    onclick={closeDeleteModal}
                    disabled={isDeleting}
                >
                    Cancel
                </button>
                <button 
                    class="flex-1 bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                    onclick={handleDeleteAccount}
                    disabled={!deletePassword || isDeleting}
                >
                    {isDeleting ? 'Deleting...' : 'Confirm Deletion'}
                </button>
            </div>
        </div>
    </div>
{/if}