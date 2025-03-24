<script>
    // Component props
    let { title, fields, component } = $props();
</script>

<div class="mb-6">
    <h2 class="text-xl font-semibold mb-3">{title}</h2>
    <div class="space-y-2">
        {#each fields as field}
            {#if component[field.key] !== undefined}
                <div class="flex justify-between border-b pb-2">
                    <span class="text-gray-600">{field.label}:</span>
                    <span class="font-medium">{component[field.key]}</span>
                </div>
            {/if}
        {/each}
    </div>
</div>