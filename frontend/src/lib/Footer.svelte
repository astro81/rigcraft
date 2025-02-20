<footer class="w-screen h-screen fixed top left-0 flex justify-center items-center text-center p-0">
    <div class="footer-container h-screen w-dvw p-8 flex justify-center items-center">
        <div class="w-dvw h-full mr-4 mt-38">

            <div>
                <div>
                    <h1 class="text-[35dvh] font-[Anton] tracking-[3.4rem]">RIGCRAFT</h1>
                </div>
            </div>

            <div class="h-full pl-24">
                <div class="h-fit grid grid-cols-2 grid-rows-1 gap-4">
                    <!-- Footer text -->
                    <div class="h-full">
                        <div class="flex justify-start px-28">
                            <div class="mr-48"><p class="text-start font-medium text-2xl p-0 m-0 leading-[1.5rem] tracking-tight">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Error inventore cum quasi animi facilis repudiandae.</p></div>
                        </div>
                    </div>
                    <!-- Footer links -->
                    <div class="h-full pl-16">
                        <div class="grid grid-cols-2 grid-rows-2 gap-y-20">

                            <div class="flex flex-col justify-start items-start pl-34">
                                <h3 class="text-3xl font-[var(--body-font)] mb-4 opacity-50">Crafts</h3>
                                <ul class="footer-items">
                                    <li><a href="/components">Explore</a></li>
                                    <li><a href="/">Build</a></li>
                                    <li><a href="/">Learn</a></li>
                                </ul>
                            </div>
                            <div class="flex flex-col justify-start items-start pl-32">
                                <h3 class="text-3xl font-[var(--body-font)] mb-4 opacity-50">Socials</h3>
                                <ul class="footer-items">
                                    <li><a href="/">Reddit</a></li>
                                    <li><a href="/">Discord</a></li>
                                    <li><a href="/">Linkden</a></li>
                                </ul>
                            </div>
                            <div class="flex flex-col justify-start items-start pl-34">
                                <h3 class="text-3xl font-[var(--body-font)] mb-4 opacity-50">Join US</h3>
                                <p class="text-2xl font-semibold">Enroll</p>
                            </div>
                            <div class="flex flex-col justify-start items-start pl-32">
                                <h3 class="text-3xl font-[var(--body-font)] mb-4 opacity-50">Copyright</h3>
                                <p class="text-xl flex gap-6"><span>© 2025</span><span>Rigcraft</span></p>
                            </div>

                        </div>
                    </div>

                </div>
            </div>

        </div>
    </div>
</footer>

<style>
    .footer-items {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
        font-family: 'Dinish Light';
        color: var(--white);
        font-size: 2em;
        font-weight: 500;
        line-height: 1.3;
        letter-spacing: 0.125rem;
        pointer-events: auto;

        li {
            margin: 0;
            padding: 0;
            display: block;
        }

        li > a {
            text-decoration: none;
            line-height: .2rem;
            margin: 0;
            padding: 0;
        }
        li > a::after{
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
        li:hover > a::after {
            transform: scaleX(1);
            transform-origin: bottom left;
        }
    }
</style>