<script>
	// import { onMount } from "svelte";

    let { src, title, description, isComingSoon } = $props();

    let hoverButtonRef = $state();
    let hoverOpacity = $state(0);
    let cursorPosition = $state({ x: 0, y: 0});

    let videoElement = $state();

    const playVideo = async () => await videoElement?.play();
    const pauseVideo = async () => await videoElement?.pause();

    const handleMouseMove = (event) => {
        if (!hoverButtonRef) return;
        const rect = hoverButtonRef.getBoundingClientRect();
        console.log("rect", rect);

        cursorPosition = {
            x: event.clientX - rect.left,
            y: event.clientY - rect.top,
        };
    };

    const handleMouseEnter = () => hoverOpacity = 1;
    const handleMouseLeave = () => hoverOpacity = 0;
</script>

<!-- svelte-ignore a11y_no_static_element_interactions -->
<div 
    class="relative size-full border-hsla border rounded-xl"
    onmouseenter={playVideo}
    onmouseleave={pauseVideo}
>
    <!-- svelte-ignore element_invalid_self_closing_tag -->
    <video
        bind:this={videoElement}
        {src}
        loop
        muted
        class="absolute left-0 top-0 size-full object-cover object-center rounded-xl"
    ></video>

    <div class="relative z-35 flex size-full flex-col justify-between p-5 text-blue-50">
        <div>
            <h1 class="font-[Dinish] text-3xl">{title}</h1>
            {#if description}
                <p class="font-[Montserrat_Variable] text-[clamp(14px,0.938vw,24px)]">{description}</p>
            {/if}
            {#if isComingSoon}
                <!-- svelte-ignore a11y_no_static_element_interactions -->
                <div
                    bind:this={hoverButtonRef}
                    onmousemove={handleMouseMove}
                    onmouseenter={handleMouseEnter}
                    onmouseleave={handleMouseLeave}
                    class="relative flex w-fit cursor-pointer items-center gap-1 overflow-hidden rounded-full bg-black px-5 py-2 text-xs uppercase text-white/20"
                    aria-label="Bento Tilt"
                >
                    <!-- Radial gradient hover effect -->
                    <div
                        class="pointer-events-none absolute -inset-px opacity-0 transition duration-300"
                        style={`
                            opacity: ${hoverOpacity};
                            background: radial-gradient(100px circle at ${cursorPosition.x}px ${cursorPosition.y}px, #656fe288, #00000026)
                        `}
                    >
                        <p class="relative z-20">coming soon</p>
                    </div>
                </div>
            {/if}    
        </div>
    </div>
</div>