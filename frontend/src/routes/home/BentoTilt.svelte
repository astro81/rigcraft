<script>
    import gsap from "gsap";

    let { children, className } = $props();

    let itemRef = $state(); // Reference for the DOM element
    let transformStyle = $state(""); // Initialize transform style

    // Handle mouse move event
    const handleMouseMove = (event) => {
        if (!itemRef) return;

        const { left, top, width, height } = itemRef.getBoundingClientRect();
        // console.log(`left: ${left}, top: ${top}, width: ${width}, height: ${height}`);

        const relativeX = (event.clientX - left) / width;
        const relativeY = (event.clientY - top) / height;

        const tiltX = (relativeY - 0.5) * 4;
        const tiltY = (relativeX - 0.5) * -4;

        // transformStyle = `perspective(700px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) scale3d(.95, .95, .95)`;
        gsap.to(itemRef, {
            duration: 0.3, // Smooth animation
            transform: `perspective(700px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) scale3d(.95, .95, .95)`,
            ease: "power2.out",
        });
    };

    // Handle mouse leave event with GSAP animation
    const handleMouseLeave = () => {
        // Reset the transform with GSAP
        gsap.to(itemRef, {
            duration: 0.5, // Smooth reset animation
            transform: "perspective(700px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)",
            ease: "power2.out",
        });
    };

</script>

<!-- svelte-ignore a11y_no_static_element_interactions -->
<div
    bind:this={itemRef}
    class={className}
    onmousemove={handleMouseMove}
    onmouseleave={handleMouseLeave}
>
    {@render children()}
</div>
