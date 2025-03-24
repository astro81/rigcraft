<script>
	import { userDataStore } from "$lib/stores/user-store.svelte";

    let isOpen = $state(false);
</script>

<header class="fixed top-0 left-0 w-full max-w-screen p-4 will-change-transform mix-blend-difference z-1000 pointer-events-none">
    <div class="header-container w-full max-w-screen flex justify-between mx-4 my-7 px-4">
        
		<div class="header-logo">
            <a href="/"><span class="cursor-default pointer-events-auto font-[Anton] text-4xl">Rigcraft</span></a>
        </div>

		<nav class="flex justify-end items-center uppercase font-bold pointer-events-auto">
            <div class="nav-container grid grid-rows-[0.3fr_1fr_0.3fr] grid-cols-[0.4rem_repeat(3,_1fr)_0.4rem] gap-x-6 gap-y-0 grid-flow-row">  <!--  An = 3 + { ((n-1)n) / 2 }, Bn = 4 + (n-1)n -->
                
                <div class="menu-corner tl border-l border-t"></div>
                <div class="menu-corner bl border-l border-b"></div>
                <div class="menu-corner tr border-r border-t"></div>
                <div class="menu-corner br border-r border-b"></div>

                <div class="menu">

                    <div class="menu-button">
                        <button
                            onclick={() => isOpen = !isOpen }
                            style:display={isOpen ? "none" : "inline-block" }
                        >Menu</button>
                        <button
                            onclick={() => isOpen = !isOpen }
                            style:display={isOpen ? "inline-block" : "none" }
                        >Close</button>
                    </div>

                    <div class="nav-wrapper" class:isOpen>
                        <ul class="nav-items flex gap-8 z-100">
                            <li class="nav-item"><a href="/categories">Explore</a></li>
                            <li class="nav-item"><a href="/builds">Builds</a></li>
                            <li class="nav-item"><a href="/forums">Forums</a></li>
                            <li class="nav-item"><a href="/support">Support</a></li>
                            {#if userDataStore.username && userDataStore.isLoggedIn}
                                <li class="nav-item"><a href="/users/{userDataStore.username}">{userDataStore.username}</a></li>
                            {:else}
                                <li class="nav-item"><a href="/users/">Login</a></li>
                            {/if}
                        </ul>
                    </div>
                </div>
                
            </div>
        </nav>

    </div>
</header>

<style>
    .nav-container {  
        grid-template-areas:
          "tl . . . tr"
          ". menu menu menu ."
          "bl . . . br";
    }

    .menu-corner {
        opacity: 0.8;
        transition: opacity 0.7s var(--expo-out);
    }
    .nav-container:hover .menu-corner {
        opacity: 0.5;
    }
    
    .tl { grid-area: tl; }

    .bl { grid-area: bl; }

    .tr { grid-area: tr; }

    .br { grid-area: br; }

    .menu { grid-area: menu; }

    .nav-items {
        .nav-item {
            display: block;
            opacity: 1;
            transition: opacity 0.8s var(--expo-out);
        }
        .nav-item:hover ~ .nav-item,
        .nav-item:not(:hover):has(+ .nav-item:hover),
        .nav-item:not(:hover):has(~ .nav-item:hover) {
            opacity: 0.4; /* Reduce opacity of siblings */
        }

        .nav-item > a {
            font-family: 'Dinish Light';
            color: var(--white);
            font-size: 1.2em;
            line-height: 1.5;
            letter-spacing: 0.0125;
            pointer-events: auto;
            display: inline-block;
            position: relative;
        }
        .nav-item > a::after{
            content: "";
            position: absolute;
            bottom: 10%;
            left: 0;
            width: 100%;
            height: 1px;
            background: var(--white);
            transform: scaleX(0);
            transform-origin: bottom left;
            transition: transform 0.3s ease-in-out;
        }
        .nav-item:hover > a::after {
            transform: scaleX(1);
            transform-origin: bottom left;
        }

    }

    /* .menu, .menu-button, .menu-button > button {
        outline: 1px solid #fff;
    } */

    .menu-button {
        margin-block: -2px;
    }

    .menu-button > button {
        font-family: 'Dinish Light', sans-serif;
        height: 1.5rem;
        width: 2.5rem;
    }

    @media (min-width: 768px) {
        .menu-button {
            display: none;
        }
    }

    @media (max-width: 768px) {
        .menu-button {
            z-index: 9999;
        }
        .nav-items {
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100%;
        }
        .header-container {
            margin: 1rem 0;
        }

        .nav-container {
            gap: 0px 0.2rem;
        }

        .nav-wrapper {
            position: absolute;
            top: -100dvh;
            left: 0;
            width: 100%;
            height: 100vh;
            background-color: aqua;
        }

        .nav-wrapper.isOpen {
            top: 10dvh;
        }
    }
    
</style>