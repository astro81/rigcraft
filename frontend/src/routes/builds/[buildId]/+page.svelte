<script>
    import { page } from '$app/stores';
    import { onMount } from 'svelte';
    import { fetchBuildDetail } from '$lib/apis/build-api';

    let build = $state(null);
    let isLoading = $state(true);
    let error = $state(null);

    onMount(async () => {
        try {
            const buildId = $page.params.buildId;
            build = await fetchBuildDetail(buildId);
        } catch (err) {
            error = err.message || 'Failed to fetch build details';
            console.error('Error fetching build details:', err);
        } finally {
            isLoading = false;
        }
    });
</script>

{#if isLoading}
    <div class="flex justify-center items-center h-screen">
        <p>Loading build details...</p>
    </div>
{:else if error}
    <div class="flex justify-center items-center h-screen text-red-500">
        <p>{error}</p>
    </div>
{:else if build}
    <div class="container mx-auto p-6">
        <h1 class="text-2xl font-bold mb-4">Build Details</h1>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="bg-white shadow rounded-lg p-4">
                <h2 class="font-semibold mb-2">CPU</h2>
                <p>{build.cpu.component_cpu_name}</p>
                <p>{build.cpu.component_cpu_details}</p>
            </div>
            <div class="bg-white shadow rounded-lg p-4">
                <h2 class="font-semibold mb-2">Memory</h2>
                <p>{build.memory.component_memory_name}</p>
                <p>{build.memory.component_memory_details}</p>
            </div>
            <div class="bg-white shadow rounded-lg p-4">
                <h2 class="font-semibold mb-2">GPU</h2>
                <p>{build.gpu.component_gpu_name}</p>
                <p>{build.gpu.component_gpu_details}</p>
            </div>
        </div>
        <div class="mt-4">
            <p class="text-sm text-gray-500">Created at: {new Date(build.created_at).toLocaleString()}</p>
        </div>
    </div>
{/if}