<script>
    import { onMount } from "svelte";
    import { leftImage, rightImage } from "$lib/assets/homeBuildsImages.js";

    const leftPerspectives = [
        { x: -10, z: -4 },
        { x: -20, z: -8 },
        { x: -30, z: -12 },
        { x: -40, z: -16 },
        { x: -50, z: -20 },
        { x: -60, z: -24 },
        { x: 10, z: -4 }
    ];
            
    const rightPerspectives = [
        { x: 10, z: -4 },
        { x: 20, z: -8 },
        { x: 30, z: -12 },
        { x: 40, z: -16 },
        { x: 50, z: -20 },
        { x: 60, z: -24 },
        { x: -10, z: -4 }
    ];

    onMount(() => {
        const leftCards = document.querySelectorAll(".left .item");
        const rightCards = document.querySelectorAll(".right .item");

        const translateImage = (target, p) => {
            target.style.transform = `translate3d(${p.x}rem, 0, ${p.z}rem)`;
        };
        
        const animateCards = (c, perspectives) => {
            const count = parseInt(c.dataset.counter);
            translateImage(c, perspectives[count - 1]);
            c.dataset.counter = (count === 7 ? 1 : count + 1).toString();
        };
        
        const interval = setInterval(() => {
            leftCards.forEach((c) => {
                animateCards(c, leftPerspectives);
            });
        
            rightCards.forEach((c) => {
                animateCards(c, rightPerspectives);
            });
        }, 1000);

        return () => clearInterval(interval);
    });
</script>

<section>
    <div class="w-full h-[90vh] relative px-12">

        <div class="flex flex-col justify-start items-center px-1 py-2">
            <h1 class="text-[clamp(38px,_3.5vw,_74px)] m-0">Explore Amazing Builds</h1>
            <h2 class="text-xl mt-1 opacity-70">Find your ture Craft, A place with limitless possiblities</h2>
        </div>

        <div class="w-full h-full flex justify-center items-center">
            <div class="gallery flex h-full w-full">
                <div class="left">
                    <div class="inner">
                        {#each leftImage as { src, counter, alt }}
                            <img 
                                class="item" 
                                {src} 
                                data-counter={counter} 
                                {alt}
                            />
                        {/each}
                    </div>
                </div>

                <div class="right">
                    <div class="inner">
                        {#each rightImage as { src, counter, alt }}
                            <img 
                                class="item" 
                                {src} 
                                data-counter={counter} 
                                {alt}
                            />
                        {/each}
                    </div>
                </div>
            </div>
        </div>            

    </div>
</section>

<style>
    .left,
    .right {
        display: flex;
        align-items: center;
        position: relative;
        overflow: hidden;
        width: 50%;
    }

    .inner {
        position: relative;
        width: 100%;
        display: flex;
        align-items: center;
        perspective: 1800px;
        transform-style: preserve-3d;
    }

    .item {
        position: absolute;
        width: 20rem;
        height: 22rem;
        transition: transform 300ms cubic-bezier(0, 0.55, 0.45, 1);
    }

    .left .inner {
        perspective-origin: right center;
    }

    .right .inner {
        perspective-origin: left center;
    }

    .left .item {
        right: -10rem;
    }

    .right .item {
        left: -10rem;
    }

    .left .item:nth-child(1) {
        transform: translate3d(-10rem, 0, -4rem);
    }

    .left .item:nth-child(2) {
        transform: translate3d(-20rem, 0, -8rem);
    }

    .left .item:nth-child(3) {
        transform: translate3d(-30rem, 0, -12rem);
    }

    .left .item:nth-child(4) {
        transform: translate3d(-40rem, 0, -16rem);
    }

    .left .item:nth-child(5) {
        transform: translate3d(-50rem, 0, -20rem);
    }

    .left .item:nth-child(6) {
        transform: translate3d(-60rem, 0, -24rem);
    }

    .left .item:nth-child(7) {
        transform: translate3d(10rem, 0, -4rem);
    }

    .right .item:nth-child(1) {
        transform: translate3d(10rem, 0, -4rem);
    }

    .right .item:nth-child(2) {
        transform: translate3d(20rem, 0, -8rem);
    }

    .right .item:nth-child(3) {
        transform: translate3d(30rem, 0, -12rem);
    }

    .right .item:nth-child(4) {
        transform: translate3d(40rem, 0, -16rem);
    }

    .right .item:nth-child(5) {
        transform: translate3d(50rem, 0, -20rem);
    }

    .right .item:nth-child(6) {
        transform: translate3d(60rem, 0, -24rem);
    }

    .right .item:nth-child(7) {
        transform: translate3d(-10rem, 0, -4rem);
    }

</style>