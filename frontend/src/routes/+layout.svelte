<script>	
	import '../app.css';
	import '@fontsource/anton';
	import '@fontsource-variable/montserrat';

	import Navbar from '$lib/components/Navbar.svelte';

	let { children } = $props();
</script>

<Navbar />

{@render children()}
