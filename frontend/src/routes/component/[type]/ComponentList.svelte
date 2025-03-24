<script>
    import { onMount } from 'svelte';
    import { fetchComponents } from './componentService';
    import ComponentCard from './ComponentCard.svelte';
    import LoadingSpinner from './LoadingSpinner.svelte';
    import ErrorMessage from './ErrorMessage.svelte';

    // Component props
    let { componentType } = $props();
    
    // Component state
    let components = $state([]);
    let isLoading = $state(true);
    let error = $state(null);

    // Load components when type changes
    $effect(() => {
        if (componentType) {
            loadComponents(componentType);
        }
    });

    // Fetch component data
    async function loadComponents(type) {
        try {
            isLoading = true;
            error = null;
            
            components = await fetchComponents(type);

            // console.log(components);
            
        } catch (err) {
            error = err.message || `Failed to fetch ${type} components`;
            console.error(`Error fetching ${type} components:`, err);
        } finally {
            isLoading = false;
        }
    }
</script>

{#if isLoading}
    <LoadingSpinner />
{:else if error}
    <ErrorMessage message={error} />
{:else if components.length === 0}
    <div class="text-center py-10">
        <p class="text-xl">No {componentType} components found</p>
    </div>
{:else}
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {#each components as component}
            <ComponentCard {component} {componentType} />
        {/each}
    </div>
{/if}

