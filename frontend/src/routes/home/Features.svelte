<script>
    import BentoCard from "./BentoCard.svelte";
	import BentoTilt from "./BentoTilt.svelte";

</script>

<section class="my-[4vw]">
    <div class="container relative w-full max-w-full py-0 px-12 mb-72">
        <div class="flex flex-col">

            <div class="px-1 py-32">
                <p class="font-[Montserrat_Variable] text-[clamp(24px,2.5vw,64px)] leading-[0.825] tracking-[-.02em] uppercase my-0">
                    The way to your Ultimate Craft
                </p>
                <p class="max-w-fit font-[Montserrat_Variable] text-xl leading-7 opacity-70 my-6">
                    Immerse yourself in a rich and ever-expanding world of computers.
                </p>
            </div>

            <div class="mx-72">
                <BentoTilt className="relative mb-7 h-96 w-full overflow-hidden md:h-[65vh]">
                    <BentoCard
                        class="bento-card"
                        src = "/videos/pc_2.mp4"
                        title={"Rigcraft"}
                        description="A world to bring forth your ultimate craft."
                    />
                </BentoTilt>

                <div class="grid h-[105vh] w-full grid-cols-2 grid-rows-2 gap-8">
                    <BentoTilt className="relative row-span-1 md:col-span-1 md:row-span-2">
                        <BentoCard
                            src="videos/pc_1.mp4"
                            title={"Aqua"}
                            description="A collection of ultimate setups."
                        />
                    </BentoTilt>
        
                    <BentoTilt className="row-span-1 ms-32 md:col-span-1 md:ms-0">
                        <BentoCard
                            src="videos/pc_3.mp4"
                            title={"Noctua"}
                            description="Embrace the true power."
                        />
                    </BentoTilt>
        
                    <BentoTilt className="me-14 md:col-span-1 md:me-0">
                        <BentoCard
                            src="videos/pc_4.mp4"
                            title={"Auros"}
                            description="Unleash the gaming beast."
                        />
                    </BentoTilt>  
                </div>
            </div>    

        </div>
    </div>
</section>
