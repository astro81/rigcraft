<!-- BuildComponentCard -->
<script>
    import { componentTypeMap } from '$lib/apis/component-api';
    import { buildStore } from '$lib/stores/build-store.svelte';
	import { buildStoreData } from '$lib/stores/builds-store.svelte';
    import { toast } from 'svelte-sonner'; // Assuming you're using a toast library

    // Component props
    let { component, componentType } = $props();

    let typeConfig = $state();
    let imageField = $state();
    let nameField = $state();
    let displayFields = $state();

    typeConfig = componentTypeMap[componentType];
    imageField = typeConfig.imageField;
    nameField = typeConfig.nameField;
    displayFields = typeConfig.displayFields;


    function handleAddComponent() {
        // Add the component to the build store
        buildStoreData[componentType] = component;
        
        // Optional: Show a toast notification
        toast.success(`Added ${component[nameField]} to build`);
    }

</script>


<div class="outline-1 w-full h-fit flex">
    <!-- Image box -->
    <div class="h-28 w-28 bg-gray-100 flex items-center justify-center">
        <img 
            src={component[imageField]}
            alt={component[nameField]}
            class="h-full object-contain"
            onerror={"this.src='/default_component.png'"}
        >
    </div>

    <!-- Info -->
    <div class="w-full grid grid-cols-10 grid-rows-1 gap-1 py-4 px-2">
        <div class="col-span-2 flex flex-wrap">
            <h2 class="text-[1rem] font-semibold">{component[nameField]}</h2>
        </div>

        <!-- Details -->
        <div class="col-span-7 flex justify-between size-full">
            {#each displayFields.slice(1) as field}
                {#if component[field.key] !== undefined}
                    <div class="flex flex-col justify-between">
                        <span class="font-medium">{field.label}:</span>
                        <span class="font-light">{component[field.key]}</span>
                    </div>
                {/if}
            {/each}
        </div>

        <!-- Details -->
        <div class="col-start-10 flex flex-col justify-between items-end px-2">
            <div class="flex justify-center items-center size-10">
                <button
                    class="border-none cursor-pointer rounded-full"
                    aria-label="component add button"
                    onclick={handleAddComponent}
                >
                    <img class="invert size-5 object-contain" src="icons/add-icon.png" alt="">
                </button>
            </div>
            <div class="flex justify-center items-center">
                <a
                    href="/component/{componentType}/{component[nameField]}"
                    aria-label="component detail button"
                >
                    <img class="invert size-10 object-contain" src="icons/bottom-arrow.png" alt="">
                </a>
            </div>
        </div>
    </div>
</div>

