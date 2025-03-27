<script>
    import { logout } from "$lib/apis/user-api";

    let { access_token, refresh_token } = $props();

    const handleLogout = async () => {
        try {
            if (!refresh_token) {
                throw new Error('Refresh token is missing.');
            }
            
            await logout(access_token, refresh_token);

            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            
            window.location.href = '/users/login';
        } catch (err) {
            console.error('Logout failed:', err);
        }
    };
</script>

<button
    type="button"
    onclick={handleLogout}
    class="flex-1 bg-transparent border border-zinc-700 text-white px-6 py-3 rounded-lg font-medium hover:border-white transition-colors"
    >
    Logout
</button>