<section 
    class="h-screen w-full relative overflow-hidden flex items-end"
    aria-label="Landing Page"
    >
    <div class="relative w-full max-w-full px-8 z-[2]">
        <div class="mb-12 mr-8 flex justify-end items-center">
            <h1 class="text-4xl flex flex-col mix-blend-difference">
                <div class="line-parent">
                    <div>Build your ultimate PC with ease.</div>
                </div>
                <div class="line-parent">
                    <div>Explore variety of components.</div>
                </div>
                <div class="line-parent">
                    <div>Compare the performances.</div>
                </div>
                <div class="line-parent">
                    <div>Start your PC-building journey today.</div>
                </div>
            </h1>
        </div>
    </div>

    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <div 
        class="h-screen w-screen absolute inset-0"
        >
        <video
            src = "/videos/pc_2.mp4"
            loop
            muted
            autoplay
            class="absolute left-0 top-0 h-screen w-screen object-cover object-center rounded-xl"
        ></video>
    </div>
</section>

<style>
    h1 {
        font-family: var(--body-font);
    }

    .line-parent {
        display: block; text-align: start; position: relative;
    }

</style>