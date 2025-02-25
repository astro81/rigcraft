<script>
    import BentoCard from "./BentoCard.svelte";
	import BentoTilt from "./BentoTilt.svelte";

</script>

<section class="my-[8vw]">
    <div class="container relative w-full max-w-full py-0 px-12 mb-82">
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
                        src = "/videos/feature-1.mp4"
                        title={"zigma"}
                        description="A cross-platform metagame app, turning your activities across Web2 and Web3 games into a rewarding adventure."
                    />
                </BentoTilt>

                <div class="grid h-[135vh] w-full grid-cols-2 grid-rows-3 gap-8">
                    <BentoTilt className="relative row-span-1 md:col-span-1 md:row-span-2">
                        <BentoCard
                            src="videos/feature-2.mp4"
                            title={"zigma"}
                            description="An anime and gaming-inspired NFT collection - the IP primed for expansion."
                        />
                    </BentoTilt>
        
                    <BentoTilt className="row-span-1 ms-32 md:col-span-1 md:ms-0">
                        <BentoCard
                          src="videos/feature-3.mp4"
                          title={"nexus"}
                          description="A gamified social hub, adding a new dimension of play to social interaction for Web3 communities."
                        />
                    </BentoTilt>
        
                    <BentoTilt className="me-14 md:col-span-1 md:me-0">
                        <BentoCard
                          src="videos/feature-4.mp4"
                          title={"azul"}
                          description="A cross-world AI Agent - elevating your gameplay to be more fun and productive."
                        />
                    </BentoTilt>
        
                    <BentoTilt className="">
                        <div class="flex size-full flex-col justify-between bg-violet-300 p-5 border-2 border-hsla rounded-xl">
                          <h1 class="bento-title special-font max-w-64 text-black">
                            M<b>o</b>re co<b>m</b>ing s<b>o</b>on.
                          </h1>      
                        </div>
                    </BentoTilt>
        
                    <BentoTilt className="">
                        <BentoCard
                            src="videos/feature-5.mp4"
                            title={"azul"}
                            description="A cross-world AI Agent - elevating your gameplay to be more fun and productive."
                        />
                    </BentoTilt>    
                </div>
            </div>    

        </div>
    </div>
</section>
