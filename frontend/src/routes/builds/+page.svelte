<script>
    import { onMount } from 'svelte';
    import { toast } from 'svelte-sonner'; 
    import { goto } from '$app/navigation';

    import { categories, initializeCategories } from "$lib/stores/category-store.svelte";
    import { fetchComponents } from "$lib/apis/component-api";

    import { createBuild } from "$lib/apis/build-api"; 
    import { buildStoreData } from '$lib/stores/builds-store.svelte';

    import BuildCategorySelector from "./BuildCategorySelector.svelte";
    import BuildComponentCard from './BuildComponentCard.svelte';
    import BuildComponentList from './BuildComponentList.svelte';

    let isLoading = $state(true);
    let error = $state({});
    
    // State for selected category and components
    let selectedCategory = $state(null);
    let components = $state([]);
    let componentsLoading = $state(false);
    let componentsError = $state(null);


    let selectedComponents = $derived({ ...buildStoreData });


    // Fetch all categories on mount
    onMount(async () => {
        try {
            isLoading = true;
            
            // Initialize categories
            const fetchedCategories = await initializeCategories();

            // Select first category by default
            if (fetchedCategories.length > 0) {
                selectedCategory = fetchedCategories[0].component_category_name;
                await loadComponents(selectedCategory);
            }
        } catch (err) {
            error = err.message || 'Failed to fetch component categories';
            console.error('Error fetching categories:', err);
        } finally {
            isLoading = false;
        }
        
    });

    // Load components for a specific category
    async function loadComponents(categoryName) {
        try {
            componentsLoading = true;
            componentsError = null;

            components = await fetchComponents(categoryName);
            selectedCategory = categoryName;
        } catch (err) {
            componentsError = err.message || `Failed to fetch ${categoryName} components`;
            console.error(`Error fetching ${categoryName} components:`, err);
        } finally {
            componentsLoading = false;
        }
    }


    async function saveBuild() {

        if (!selectedComponents.cpu || !selectedComponents.memory || !selectedComponents.gpu) {
            toast.error('Please select a CPU, Memory, and GPU before saving the build');
            return;
        } else {
            console.log('Component Selected');
        }

        const access_token = localStorage.getItem('access_token');

        if (!access_token) {
            toast.error('You must be logged in to save a build');
            alert('You must be logged in to save a build');
            return;
        }

        try {
            const buildData = {
                cpu: selectedComponents.cpu.component_cpu_id,
                memory: selectedComponents.memory.component_memory_id,
                gpu: selectedComponents.gpu.component_gpu_id
            };

            console.log('Sending build data:', buildData); // Log the data being sent

            const savedBuild = await createBuild(buildData, access_token);

            toast.success('Build saved successfully!');
            alert("Build saved");

            // Redirect to the build details page
            // goto(`/builds/${savedBuild.id}`);

            // reset the build store
            buildStoreData.cpu = null;
            buildStoreData.memory = null;
            buildStoreData.gpu = null;

        } catch (err) {
            console.error('Full error object:', err);
            console.error('Error response:', err.response);
            toast.error(`Failed to save build: ${err.response?.data?.detail || err.message}`);
        }

    }

</script>


<section class="flex justify-center items-center h-screen w-screen pt-26 pb-8">
    <div class="size-full mx-8 flex justify-center items-center outline-[var(--border-color)] outline-1">
        <div class="size-full grid grid-rows-1 grid-cols-8">
            <!-- Components selector -->
            <div class="size-full flex overflow-clip">
                <div class="category-box flex flex-col overflow-y-clip">
                    <!-- svelte-ignore a11y_click_events_have_key_events -->
                    {#each categories as category}
                        <!-- svelte-ignore a11y_click_events_have_key_events -->
                        <!-- svelte-ignore a11y_no_static_element_interactions -->
                        <div onclick={() => loadComponents(category.component_category_name)}>
                            <BuildCategorySelector 
                                {...category} 
                                active={selectedCategory === category.component_category_name}
                            />
                        </div>
                    {/each}
                </div>
            </div>
            
            <div class="size-full col-span-7 p-6 border-l-1 grid grid-cols-1 grid-rows-10 gap-4">
                <div class="outline-1 outline-[var(--border-color)] size-full overflow-auto row-span-9">
                    <!-- Components List -->
                    {#if componentsLoading}
                        <div class="flex justify-center items-center h-full">
                            <p>Loading components...</p>
                        </div>
                    {:else if componentsError}
                        <div class="flex justify-center items-center h-full text-red-500">
                            <p>{componentsError}</p>
                        </div>
                    {:else if components.length === 0}
                        <div class="flex justify-center items-center h-full">
                            <p>No components found</p>
                        </div>
                    {:else}
                        <BuildComponentList {components} {selectedCategory}/>
                    {/if}
                </div>

                <div class="outline-1 outline-[var(--border-color)] size-full row-start-10 flex justify-between items-center">
                    <!-- Selected Components Summary -->
                    <div class="flex ml-4 space-x-4">
                        <div>
                            <strong>CPU:</strong> 
                            {selectedComponents.cpu ? selectedComponents.cpu.component_cpu_name : 'Not selected'}
                        </div>
                        <div>
                            <strong>Memory:</strong> 
                            {selectedComponents.memory ? selectedComponents.memory.component_memory_name : 'Not selected'}
                        </div>
                        <div>
                            <strong>GPU:</strong> 
                            {selectedComponents.gpu ? selectedComponents.gpu.component_gpu_name : 'Not selected'}
                        </div>
                    </div>

                    <!-- build save button -->
                    <div class="m-4 outline-1">
                        <button 
                            class="outline-1 size-full px-4 py-2 cursor-pointer"
                            onclick={saveBuild}
                        >
                            Save Build
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>


