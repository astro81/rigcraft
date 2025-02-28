<script>
    import { ComponentCpuStore } from "$lib/stores/component-store.svelte.js";
    /** @type {{ data: import('./$types.js').PageData }} */
    let { data } = $props();

    let component = ComponentCpuStore.find(component => component.name == data.name);
</script>

<section class="w-screen h-screen">
    <div class="w-full h-full flex justify-center items-center">
        
        <div class="flex flex-col">
            {#if component}
                <h1>Component Name = {component.name}</h1>
                <h1>Component Price = {component.price}</h1>
                <h1>Component Boost Clock = {component.boost_clock}</h1>
                <h1>Component Cores = {component.core_count}</h1>
            {:else}
                <h1>Component with id {data.name} not found</h1>
            {/if}
        </div>
        
    </div>
</section>

<style>
    h1 {
        color: whitesmoke;
        font-size: 1.5rem;
    }
</style>