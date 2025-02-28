<script>
    import { ComponentCpuStore } from "$lib/stores/component-store.svelte.js";
    import ComponentCard from "./ComponentCard.svelte";
</script>

<section class="w-full">
    <div class="w-full h-full flex justify-center items-center">
        <div class="mt-36 w-full px-40">
            <div class="cards">
                {#each ComponentCpuStore as component}
                    <ComponentCard {...component} />
                {/each}
            </div>
        </div>
    </div>
</section>

<style>
    .cards {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1.5rem;
        padding: 2rem;
    }
</style>