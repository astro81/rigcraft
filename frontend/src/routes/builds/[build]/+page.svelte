<script>
    import { page } from '$app/stores';
    import { onMount } from 'svelte';
    import { fetchUserBuilds } from '$lib/apis/build-api';
    import { fetchComponentDetail } from '$lib/apis/component-api';

    let build = $state(null);
    let isLoading = $state(true);
    let error = $state(null);
    let cpuDetail = $state(null);
    let memoryDetail = $state(null);
    let gpuDetail = $state(null);

    let { data } = $props();

    onMount(async () => {
        try {
            const access_token = localStorage.getItem('access_token');

            if (!access_token) {
                toast.error('You must be logged in to view a build');
                alert('You must be logged in to view a build');
                return;
            }
            const buildId = data.buildId;
            
            // First fetch the build which contains component IDs
            build = await fetchUserBuilds(buildId, access_token);
            console.log('Build data:', build);

            // Then fetch details for each component
            if (build) {
                // Fetch CPU details
                if (build.cpu) {
                    cpuDetail = await fetchComponentDetail('cpu', build.cpu);
                    console.log('CPU details:', cpuDetail);
                }

                // Fetch Memory details
                if (build.memory) {
                    memoryDetail = await fetchComponentDetail('memory', build.memory);
                    console.log('Memory details:', memoryDetail);
                }

                // Fetch GPU details
                if (build.gpu) {
                    gpuDetail = await fetchComponentDetail('gpu', build.gpu);
                    console.log('GPU details:', gpuDetail);
                }
            }

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
{:else if build && cpuDetail && memoryDetail && gpuDetail}
    <div class="container mx-auto p-6">
        <h1 class="text-3xl font-bold mb-6">Build Details</h1>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <!-- CPU Details -->
            <div class="shadow-lg rounded-lg p-6 outline-1">
                <h2 class="text-2xl font-semibold mb-4 border-b pb-2">CPU</h2>
                <div class="space-y-3">
                    <div>
                        <strong class="text-gray-600">Name:</strong>
                        <p>{cpuDetail.component_cpu_name}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Brand:</strong>
                        <p>{cpuDetail.component_cpu_brand}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Model:</strong>
                        <p>{cpuDetail.component_cpu_model}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Series:</strong>
                        <p>{cpuDetail.component_cpu_series}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Socket:</strong>
                        <p>{cpuDetail.component_cpu_socket}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Cores:</strong>
                        <p>{cpuDetail.component_cpu_cores}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Threads:</strong>
                        <p>{cpuDetail.component_cpu_threads}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Clock Speed:</strong>
                        <p>{cpuDetail.component_cpu_clock_speed} GHz</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Price:</strong>
                        <p>{formatCurrency(cpuDetail.component_cpu_price)}</p>
                    </div>
                    {#if cpuDetail.component_cpu_image}
                    <div>
                        <strong class="text-gray-600">Image:</strong>
                        <img src={cpuDetail.component_cpu_image} alt={cpuDetail.component_cpu_name} class="mt-2 w-32 h-32 object-contain" />
                    </div>
                    {/if}
                </div>
            </div>



            <!-- Memory Details -->
            <div class="shadow-lg rounded-lg p-6 outline-1">
                <h2 class="text-2xl font-semibold mb-4 border-b pb-2">Memory</h2>
                <div class="space-y-3">
                    <div>
                        <strong class="text-gray-600">Name:</strong>
                        <p>{memoryDetail.component_memory_name}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Producer:</strong>
                        <p>{memoryDetail.component_memory_producer}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Model:</strong>
                        <p>{memoryDetail.component_memory_model}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Type:</strong>
                        <p>{memoryDetail.component_memory_type}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Size:</strong>
                        <p>{memoryDetail.component_memory_size} GB</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Clock Speed:</strong>
                        <p>{memoryDetail.component_memory_clock_speed} MHz</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Price:</strong>
                        <p>{formatCurrency(memoryDetail.component_memory_price)}</p>
                    </div>
                    {#if memoryDetail.component_memory_image}
                    <div>
                        <strong class="text-gray-600">Image:</strong>
                        <img src={memoryDetail.component_memory_image} 
                            alt={memoryDetail.component_memory_name} 
                            class="mt-2 w-32 h-32 object-contain" />
                    </div>
                    {/if}
                </div>
            </div>

            <!-- GPU Details -->
            <div class="shadow-lg rounded-lg p-6 outline-1">
                <h2 class="text-2xl font-semibold mb-4 border-b pb-2">GPU</h2>
                <div class="space-y-3">
                    <div>
                        <strong class="text-gray-600">Name:</strong>
                        <p>{gpuDetail.component_gpu_name}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Brand:</strong>
                        <p>{gpuDetail.component_gpu_brand}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Series:</strong>
                        <p>{gpuDetail.component_gpu_series}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Model:</strong>
                        <p>{gpuDetail.component_gpu_model}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">VRAM:</strong>
                        <p>{gpuDetail.component_gpu_vram} GB</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Boost Clock:</strong>
                        <p>{gpuDetail.component_gpu_boost_clock} MHz</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Power Consumption:</strong>
                        <p>{gpuDetail.component_gpu_power_consumption} W</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">HDMI Ports:</strong>
                        <p>{gpuDetail.component_gpu_hdmi_port}</p>
                    </div>
                    <div>
                        <strong class="text-gray-600">Price:</strong>
                        <p>{formatCurrency(gpuDetail.component_gpu_price)}</p>
                    </div>
                    {#if gpuDetail.component_gpu_image}
                    <div>
                        <strong class="text-gray-600">Image:</strong>
                        <img src={gpuDetail.component_gpu_image} 
                            alt={gpuDetail.component_gpu_name} 
                            class="mt-2 w-32 h-32 object-contain" />
                    </div>
                    {/if}
                </div>
            </div>
        </div>

        <div class="mt-6 shadow-lg rounded-lg p-6 outline-1">
            <h2 class="text-2xl font-semibold mb-4 border-b pb-2">Build Summary</h2>
            <div class="grid grid-cols-2 gap-4">
                <div>
                    <strong class="text-gray-600">Total Build Cost:</strong>
                    <p>{formatCurrency(
                        Number(cpuDetail.component_cpu_price) + 
                        Number(memoryDetail.component_memory_price) + 
                        Number(gpuDetail.component_gpu_price)
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