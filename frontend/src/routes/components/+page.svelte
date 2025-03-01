<script>
    import { CategoryStore } from "$lib/stores/category-store.svelte.js";
	import CategoryCard from "./CategoryCard.svelte";

    
</script>

<section class="w-screen h-fit">
    <div class="w-full flex justify-center items-center absolute top-0 left-0 outline-1">
        <div class="max-w-[90%] w-full h-full flex justify-center items-center mt-36 overflow-hidden">

            <div class="container">
                {#each CategoryStore as category}
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