<script>
</script>

<header class="fixed top-0 left-0 w-full max-w-screen py-8 px-0 will-change-transform mix-blend-difference pointer-events-none z-1000">
    <div class="w-full max-w-screen ml-auto mr-auto py-4 px-12 flex justify-between">

        <div class="header-logo">
            <a href="/" aria-label="Go to homepage">
                <span class="font-bold">RIGCRAFT</span>
            </a>
        </div>

        <nav class="flex justify-end items-center uppercase font-bold">
            <div class="relative pointer-events-auto">
                <div class="borders-left"></div>
                <div class="borders-right"></div>

                <ul class="header-nav flex m-0 p-0 ms-0 me-0 px-4">
                    <li>
                        <div><a href="/about">About</a></div>
                    </li>
                    <li>
                        <div><a href="/projects">Projects</a></div>
                    </li>
                    <li>
                        <div><a href="/news">News</a></div>
                    </li>
                    <li>
                        <div><a href="/contact">Contact</a></div>
                    </li>
                    <li>
                        <div><a href="/carrers">Carrers</a></div>
                    </li>
                </ul>

            </div>
        </nav>

    </div>
</header>


<style>
    :root {
        --menu-border-width: 0.45rem;
    }

    .header-logo > a > span {
        /* font-size: clamp(48px, 8vw, 180px); */
        font-size: 2dvw;
    }

    .borders-left, .borders-right {
        opacity: 0.625;
        pointer-events: none;
    }

    .borders-left::before, .borders-left::after,
    .borders-right::before, .borders-right::after {
        content: "";
        height: var(--menu-border-width);
        width: var(--menu-border-width);
        position: absolute;
        display: block;
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


    .header-nav {
        margin-block-start: .2em;
        margin-block-end: .2em;

        li {
            margin: 0 1rem;
            position: relative;
        }

        li > div > a {
            color: var(--white);
            font-size: 1.2em;
            line-height: 1.5;
            letter-spacing: 0.0125em;
            pointer-events: auto;
            display: block;
            opacity: 1;
            transition: opacity 1s var(--expo-out);
            text-decoration: none;
        }
    }
</style>
