<!-- ComponentListPage -->
<script>
    import ComponentList from './ComponentList.svelte';

    // Component props
    let { data } = $props();
    let componentType = data.component_type;
</script>

<section class="w-full py-12 px-4">
    <div class="max-w-7xl mx-auto">
        <!-- Header -->
        <div class="mb-8">
            <h1 class="text-3xl font-bold capitalize">{componentType} Components</h1>
            <p class="text-lg mt-2 opacity-70">
                Browse all available {componentType} components
            </p>
        </div>

        <!-- Component List -->
        <ComponentList {componentType} />
    </div>
</section>

