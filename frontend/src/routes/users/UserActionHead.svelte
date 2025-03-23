<script>
    let { isLoginFormVisible } = $props();
</script>

<div class="absolute top-0 left-1/2 -translate-x-1/2 flex items-center justify-center w-[140px] h-[50px]">
    <div class="relative">
        <div class="absolute left-1/2 -translate-x-1/2 -translate-y-1/2 text-white text-2xl transition-all duration-300"
            style:top={isLoginFormVisible ? '50%' : '-60px'} 
            style:opacity={isLoginFormVisible ? 1 : 0}>Login</div>
        <div class="absolute left-1/2 -translate-x-1/2 -translate-y-1/2 text-white text-2xl transition-all duration-300"
            style:top={isLoginFormVisible ? '50px' : '50%'} 
            style:opacity={isLoginFormVisible ? 0 : 1}>Register</div>
    </div>
</div>