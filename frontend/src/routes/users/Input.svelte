<script>
    let { type, placeholder, value = $bindable() } = $props();
</script>

<input 
    {type}
    {placeholder} 
    bind:value={value}
    class="w-full h-[55px] text-base bg-transparent text-white px-5 border border-[var(--border-color)] rounded-[30px] outline-none transition-all duration-300 focus:border-white active:border-amber-50 focus:outline-amber-50 active:outline-amber-50" 
>