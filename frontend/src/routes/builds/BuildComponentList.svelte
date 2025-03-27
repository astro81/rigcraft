<!-- BuildComponentList -->
<script>
    import BuildComponentCard from "./BuildComponentCard.svelte";

    let { components, selectedCategory } = $props();

</script>

<div class="flex flex-col justify-center gap-4 p-4">
    {#each components as component}
        <BuildComponentCard 
            component={component} 
            componentType={selectedCategory} 
        />
    {/each}
</div>

