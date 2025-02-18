<header class="fixed top-0 left-0 w-full max-w-screen p-4 will-change-transform mix-blend-difference z-1000 pointer-events-none">
    <div class="header-contaienr w-full max-w-screen flex justify-between mx-4 my-7 px-4">
        
		<div class="header-logo">
            <a href="/"><span class="cursor-default pointer-events-auto font-[Anton] text-4xl">Rigcraft</span></a>
        </div>

		<nav class="flex justify-end items-center uppercase font-bold mx-8">
            <div class="nav-wrapper relative pointer-events-auto">

                <div class="borders-left"></div>
                <div class="borders-right"></div>

                <ul class="nav-container flex px-5">
                    <li class="nav-items"><a href="/components">Explore</a></li>
                    <li class="nav-items"><a href="/builds">Builds</a></li>
                    <li class="nav-items"><a href="/forums">Forums</a></li>
                    <li class="nav-items"><a href="/support">Support</a></li>
                    <li class="nav-items"><a href="/user">Login</a></li>
                </ul>

            </div>
        </nav>

    </div>
</header>

<style>
	/* header, .header-logo{
		outline: 1px solid #fff;
	} */

    :root {
        --border-width: 0.4rem;
    }

    .borders-left::before, .borders-left::after,
    .borders-right::before, .borders-right::after {
        content: "";
        height: var(--border-width);
        width: var(--border-width);
        position: absolute;
        display: block;
    }

    .nav-wrapper .borders-left,
    .nav-wrapper .borders-right {
        opacity: 0.6;
        transition: opacity 0.8s var(--expo-out);
    }

    .nav-wrapper:hover .borders-left,
    .nav-wrapper:hover .borders-right {
        opacity: 0.4; 
    }

    .borders-left::before {
        border-left: 1px solid var(--white);
        border-top: 1px solid var(--white);
        left: 0px;
        top: 0px;
    }

    .borders-left::after {
        border-left: 1px solid var(--white);
        border-bottom: 1px solid var(--white);
        left: 0px;
        bottom: 0px;
    }

    .borders-right::before {
        border-right: 1px solid var(--white);
        border-top: 1px solid var(--white);
        right: 0px;
        top: 0px;
    }

    .borders-right::after {
        border-right: 1px solid var(--white);
        border-bottom: 1px solid var(--white);
        right: 0px;
        bottom: 0px;
    }

    .nav-container {
        .nav-items {
            position: relative;
            margin: 0.3rem 1rem;
        }

        .nav-items > a {
            color: var(--white);
            font-size: 1.2em;
            line-height: 1.5;
            letter-spacing: 0.0125;
            pointer-events: auto;
            display: block;
            font-family: 'Dinish Light';
            /* margin-inline-start: 1rem;
            margin-inline-end: 1rem; */
        }

        .nav-items > a::after {
            content: '';
            position: absolute;
            width: 100%;
            transform: scaleX(0);
            height: 1px;
            bottom: 10%;
            left: 0;
            background-color: var(--white);
            transition: transform 1s var(--expo-out);
            transform-origin: bottom left;
        }
        .nav-items:hover > a::after {
            transform: scaleX(1);
            transform-origin: bottom left;
        }
    }
</style>