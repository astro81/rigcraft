<script>
    import { componentCategoryStore } from "$lib/stores/category-store.svelte.js";
	import { onMount } from "svelte";
	import CategoryCard from "./CategoryCard.svelte";

    onMount(async function () {
        if (!componentCategoryStore.length) {
            const categoryApiEndpoint = 'http://127.0.0.1:8000/api/component_category/';
            const response = await fetch(categoryApiEndpoint);
            const categoryDataArray = await response.json();
            categoryDataArray.forEach(categoryObj => { componentCategoryStore.push(categoryObj) });
        }
    });
</script>

<section class="w-screen h-fit">
    <div class="w-full flex justify-center items-center absolute top-0 left-0">
        <div class="max-w-[90%] w-full h-full flex justify-center items-center mt-36 overflow-hidden">

            <div class="container">
                {#each componentCategoryStore as category}
                    <CategoryCard {...category}/>
                {/each}

            </div>

        </div>
    </div>
</section>

<style>
    .container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
        justify-content: center;
    }
</style>