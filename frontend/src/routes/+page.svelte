<script>
    import Hero from "./home/Hero.svelte";
    import Comps from "./home/Crafts.svelte";
	import Footer from "$lib/components/Footer.svelte";
	import Features from "./home/Features.svelte";
	import BuildSlides from "./home/BuildSlides.svelte";
</script>

<div class="site-wrapper">
    <main class="absolute z-[1]">
        <div class="flex flex-col bg-black mb-[100dvh]">
            <Hero />
            <Comps />
            <Features />
            <BuildSlides />
        </div>
    </main>
    <Footer />
</div>