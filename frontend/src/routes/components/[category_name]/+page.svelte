<script>
    /** @type {{ data: import('./$types').PageData }} */
    let { data } = $props();
    $inspect(data);
</script>

<h1 class="text-white">{data.name}</h1>