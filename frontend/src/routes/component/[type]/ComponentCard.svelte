<script>
    import { componentTypeMap } from './componentService';

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
    
</script>

<div class="border rounded-lg overflow-hidden shadow-sm hover:shadow-md transition-shadow">
    <!-- Component Image -->
    <div class="h-48 bg-gray-100 flex items-center justify-center">
        <img 
            src={component[imageField]} 
            alt={component[nameField]}
            class="h-full object-contain"
            onerror={"this.src='/default_component.png'"}
        />
    </div>
    
    <!-- Component Info -->
    <div class="p-4">
        <h2 class="text-xl font-semibold mb-2">
            {component[nameField]}
        </h2>
        
        <div class="space-y-1">
            {#each displayFields.slice(1) as field}
                {#if component[field.key] !== undefined}
                    <div class="flex justify-between">
                        <span class="text-gray-600">{field.label}:</span>
                        <span class="font-medium">{component[field.key]}</span>
                    </div>
                {/if}
            {/each}
        </div>
        
        <div class="mt-4">
            <a 
                href="/component/{componentType}/{component[nameField]}" 
                class="block w-full py-2 px-4 bg-blue-600 text-white text-center rounded hover:bg-blue-700 transition-colors"
            >
                View Details
            </a>
        </div>
    </div>
</div>

