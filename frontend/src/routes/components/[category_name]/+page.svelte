<script>
    import { componentCategoryStore } from "$lib/stores/category-store.svelte.js";
	import { onMount } from "svelte";
	import ComponentCard from "./ComponentCard.svelte";

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

<section class="w-screen h-fit">
    <div class="w-full flex justify-center items-center absolute top-0 left-0">
        <div class="max-w-[90%] w-full h-full flex flex-col justify-center items-center mt-36 overflow-hidden">

            <div class="fixed top-0 left-0 w-full h-[20dvh] flex justify-center items-center pt-18 bg-black">
                <div class="flex flex-col justify-center items-start w-full my-8 mx-105">
                    {#if category}
                        <h1 class="text-5xl font-normal">{category.component_category_title}</h1>
                        <h1 class="text-xl font-normal mt-2 opacity-60">{category.component_category_sub_title}</h1>
                    {:else}
                        <p>The category does not exist {data.component_category_name}</p>
                    {/if}
                </div>
            </div>

            <div class="container flex flex-col gap-4 mt-38">

                <ComponentCard />
                <ComponentCard />
                <ComponentCard />
                <ComponentCard />
                <ComponentCard />
                <ComponentCard />
                <ComponentCard />
                <ComponentCard />
                <ComponentCard />
                <ComponentCard />
                <ComponentCard />
                <ComponentCard />

            </div>

        </div>
    </div>
</section>