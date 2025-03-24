<script>
    import { onMount } from 'svelte';
    import { componentTypeMap, fetchComponentDetail } from '../componentService';
    import { componentDetailConfig } from './componentDetailConfig';
    import LoadingSpinner from '../LoadingSpinner.svelte';
    import ErrorMessage from '../ErrorMessage.svelte';
    import ComponentDetailSection from './ComponentDetailSection.svelte';

    // Component props
    let { componentType, componentName } = $props();
    
    // Component state
    let component = $state(null);
    let isLoading = $state(true);
    let error = $state(null);

    let typeConfig = $state();
    let detailConfig = $state();
    let imageField = $state();
    let nameField = $state();
    let displayGroups = $state();

    // Get configuration for the current component type
    typeConfig = componentTypeMap[componentType];
    detailConfig = componentDetailConfig[componentType];
    // svelte-ignore state_referenced_locally
        imageField = typeConfig?.imageField;
    // svelte-ignore state_referenced_locally
        nameField = typeConfig?.nameField;
    // svelte-ignore state_referenced_locally
        displayGroups = detailConfig?.displayGroups || [];

    // Load component when type or name changes
    $effect(() => {
        
        if (componentType && componentName) {
            loadComponentDetail();
        }
    });

    // Fetch component detail data
    async function loadComponentDetail() {
        try {
            isLoading = true;
            error = null;
            
            component = await fetchComponentDetail(componentType, componentName);
            
        } catch (err) {
            error = err.message || `Failed to fetch component details`;
            console.error(`Error fetching component details:`, err);
        } finally {
            isLoading = false;
        }
    }
</script>

{#if isLoading}
    <LoadingSpinner />
{:else if error}
    <ErrorMessage message={error} />
{:else if component}
    <div class="bg-white rounded-lg shadow overflow-hidden">
        <!-- Component Header -->
        <div class="p-6 border-b">
            <h1 class="text-3xl font-bold">{component[nameField]}</h1>
        </div>
        
        <div class="md:flex">
            <!-- Component Image -->
            <div class="md:w-1/3 p-6 flex justify-center">
                <img 
                    src={component[imageField]} 
                    alt={component[nameField]}
                    class="max-w-full h-auto object-contain max-h-64"
                    onerror={"this.src='/default_component.png'"}
                />
            </div>
            
            <!-- Component Details -->
            <div class="md:w-2/3 p-6">
                {#each displayGroups as group}
                    <ComponentDetailSection 
                        title={group.title} 
                        fields={group.fields} 
                        {component} 
                    />
                {/each}
                
                <!-- Add to build (Placeholder for functionality) -->
                <div class="mt-8">
                    <button class="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 px-6 rounded-lg font-medium transition-colors">
                        Add to Build
                    </button>
                </div>
            </div>
        </div>
    </div>
{:else}
    <div class="text-center py-10">
        <p class="text-xl">Component not found</p>
    </div>
{/if}