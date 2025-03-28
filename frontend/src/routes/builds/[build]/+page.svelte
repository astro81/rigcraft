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
            console.log('Full build details:', build);
        } catch (err) {
            error = err.message || 'Failed to fetch build details';
            console.error('Error fetching build details:', err);
        } finally {
            isLoading = false;
        }
    });

    // Helper function to format currency
    function formatCurrency(value) {
        return new Intl.NumberFormat('en-US', { 
            style: 'currency', 
            currency: 'USD' 
        }).format(value);
    }
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
        <h1 class="text-3xl font-bold mb-6">Build Details</h1>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <!-- CPU Details -->
            <div class="shadow-lg rounded-lg p-6 outline-1">
                <h2 class="text-2xl font-semibold mb-4 border-b pb-2">CPU</h2>
                <div class="space-y-3">
                    <div>
                        <strong class="text-gray-600">Name:</strong>
                        <p>{build.cpu.component_cpu_name}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Brand:</strong>
                        <p>{build.cpu.brand}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Model:</strong>
                        <p>{build.cpu.model}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Cores:</strong>
                        <p>{build.cpu.cores}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Clock Speed:</strong>
                        <p>{build.cpu.clock_speed} GHz</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Price:</strong>
                        <p>{formatCurrency(build.cpu.price)}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Details:</strong>
                        <p>{build.cpu.component_cpu_details}</p>
                    </div>
                </div>
            </div>

            <!-- Memory Details -->
            <div class="shadow-lg rounded-lg p-6 outline-1">
                <h2 class="text-2xl font-semibold mb-4 border-b pb-2">Memory</h2>
                <div class="space-y-3">
                    <div>
                        <strong class="text-gray-600">Name:</strong>
                        <p>{build.memory.component_memory_name}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Brand:</strong>
                        <p>{build.memory.brand}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Capacity:</strong>
                        <p>{build.memory.capacity} GB</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Type:</strong>
                        <p>{build.memory.type}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Speed:</strong>
                        <p>{build.memory.speed} MHz</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Price:</strong>
                        <p>{formatCurrency(build.memory.price)}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Details:</strong>
                        <p>{build.memory.component_memory_details}</p>
                    </div>
                </div>
            </div>

            <!-- GPU Details -->
            <div class="shadow-lg rounded-lg p-6 outline-1">
                <h2 class="text-2xl font-semibold mb-4 border-b pb-2">GPU</h2>
                <div class="space-y-3">
                    <div>
                        <strong class="text-gray-600">Name:</strong>
                        <p>{build.gpu.component_gpu_name}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Brand:</strong>
                        <p>{build.gpu.brand}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Model:</strong>
                        <p>{build.gpu.model}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Memory:</strong>
                        <p>{build.gpu.memory} GB</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Clock Speed:</strong>
                        <p>{build.gpu.clock_speed} MHz</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Price:</strong>
                        <p>{formatCurrency(build.gpu.price)}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Details:</strong>
                        <p>{build.gpu.component_gpu_details}</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="mt-6 shadow-lg rounded-lg p-6 outline-1">
            <h2 class="text-2xl font-semibold mb-4 border-b pb-2">Build Summary</h2>
            <div class="grid grid-cols-2 gap-4">
                <div>
                    <strong class="text-gray-600">Total Build Cost:</strong>
                    <p>{formatCurrency(
                        Number(build.cpu.price) + 
                        Number(build.memory.price) + 
                        Number(build.gpu.price)
                    )}</p>
                </div>
                <div>
                    <strong class="text-gray-600">Created At:</strong>
                    <p>{new Date(build.created_at).toLocaleString()}</p>
                </div>
            </div>
        </div>
    </div>
{/if}

