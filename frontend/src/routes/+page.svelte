<script>
    import Hero from "./home/Hero.svelte";
    import Comps from "./home/Comps.svelte";
	import Footer from "$lib/Footer.svelte";
</script>

<div class="site-wrapper">
    <!-- <main class="relative z-20">
        <Hero />
        <Comps />
    </main>
    <footer class="fixed bottom-0 -z-10">
        <h1 class="text-7xl">Foot</h1>
    </footer> -->

    <main class="absolute z-[1]">
        <div class="flex flex-col bg-black mb-[100dvh]">
            <Hero />
            <Comps />
        </div>
        <!-- <div class="w-full h-screen bg-[rgb(255,0,0,1)]"></div> -->
    </main>
    <Footer />
      
</div>
