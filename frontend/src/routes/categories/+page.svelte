<script>
    import { onMount } from 'svelte'; 
    import { categories, initializeCategories } from '$lib/stores/category-store.svelte';
    import CategoryCard from './CategoryCard.svelte';

    let isLoading = $state(true);
    let error = $state({});

    // Fetch all categories on mount
    onMount(async () => {
        try {
            isLoading = true;
            
            // Initialize categories
            await initializeCategories();
        } catch (err) {
            error = err.message || 'Failed to fetch component categories';
            console.error('Error fetching categories:', err);
        } finally {
            isLoading = false;
        }
    });
</script>

<section class="w-screen h-fit">
    <div class="w-full flex justify-center items-center absolute top-0 left-0">
        <div class="max-w-[90%] w-full h-full flex justify-center items-center mt-36 overflow-hidden">
            <div class="container">
                {#each categories as category}
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