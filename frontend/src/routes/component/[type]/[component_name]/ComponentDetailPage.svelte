<script>
    import ComponentDetail from './ComponentDetail.svelte';

    // Component props
    let { data } = $props();
    let componentType = data.component_type;
    let componentName = data.component_name;
</script>

<section class="w-full py-12 px-4">
    <div class="max-w-4xl mx-auto">
        <!-- Back button -->
        <div class="mb-6">
            <a href="/component/{componentType}" class="inline-flex items-center text-blue-600 hover:text-blue-800">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M9.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L7.414 9H15a1 1 0 110 2H7.414l2.293 2.293a1 1 0 010 1.414z" clip-rule="evenodd" />
                </svg>
                Back to {componentType} list
            </a>
        </div>
        
        <!-- Component Detail -->
        <ComponentDetail {componentType} {componentName} />
    </div>
</section>