<script>
    import { componentCategoryStore } from "$lib/stores/category-store.svelte.js";
	import { onMount } from "svelte";

    let { data } = $props();

    let category = $state();

    onMount(async function () {
        if (!componentCategoryStore.length){
            category = componentCategoryStore.find(category => category.component_category_name == data.name);
        } else {
            const endpoint = `http://127.0.0.1:8000/api/component_category/${data.name}`;
            let response = await fetch(endpoint);
            if (response.status == 200) {
                category = await response.json();
            } else {
                category = null;
            }
        }
    })

</script>

{#if category}
    <h1>{category.component_category_title}</h1>
    <h1>{category.component_category_sub_title}</h1>
{:else}
    <p>The category does not exis {data.component_category_name}</p>
{/if}