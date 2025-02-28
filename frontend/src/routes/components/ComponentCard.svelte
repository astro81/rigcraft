<script>
    let component = $props();
</script>

<div class="card">
    <div>
        {#if component.name.includes("AMD")}
            <img src="assets/amd.png" alt="AMD CPU">
        {:else if component.name.includes("Intel")}
            <img src="assets/intel.png" alt="Intel CPU">
        {:else}
            <img src="assets/cpu.png" alt="Generic CPU">
        {/if}
    </div>
    <div>
        <h1>{component.name}</h1>
        <h1>{component.type}</h1>
    </div>
</div>

<style>
    .card {
        break-inside: avoid;
        margin-bottom: 1.5rem;
        border: 2px solid;
        /* padding: 1rem; */
        display: flex;
        flex-direction: column;
    }

    img {
        width: 100%;
        /* margin-bottom: 1rem; */
        transform-style: preserve-3d;
    }
</style>