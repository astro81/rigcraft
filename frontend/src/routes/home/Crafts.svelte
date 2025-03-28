<script>
    import { onMount } from 'svelte';
    import { gsap } from 'gsap';

    let sliderContent;
    let items = [];
    const itemWidth = 300 + 32; // width + margin
    let currentIndex = 0;

    onMount(() => {
      // Clone first and last items for seamless looping
    const firstItem = items[0];
    const lastItem = items[items.length - 1];

      // Prepend last item clone
    const lastClone = lastItem.cloneNode(true);
    sliderContent.insertBefore(lastClone, firstItem);
    
    // Append first item clone
    const firstClone = firstItem.cloneNode(true);
    sliderContent.appendChild(firstClone);
    
    // Set initial position (offset by one item since we prepended)
    gsap.set(sliderContent, { x: -itemWidth });
    });

    function prevBtn() {
        currentIndex--;
        animateToIndex();
    }

    function nextBtn() {
        currentIndex++;
        animateToIndex();
    }

    function animateToIndex() {
        gsap.to(sliderContent, {
            x: -(currentIndex + 1) * itemWidth, // +1 accounts for prepended clone
            duration: 0.8,
            ease: 'power3.out',
            onComplete: checkLoop
        });
    }

    function checkLoop() {
      // If at the end (cloned first item), jump to real first item
        if (currentIndex >= items.length) {
            currentIndex = 0;
            gsap.set(sliderContent, { x: -itemWidth });
        } 
        // If at the beginning (cloned last item), jump to real last item
        else if (currentIndex < 0) {
            currentIndex = items.length - 1;
            gsap.set(sliderContent, { x: -(items.length) * itemWidth });
        }
    }
  </script>
  
  <section class="my-[8vw]">
      <div class="relative w-full max-w-full py-0 px-12">
          <div class="seperator block absolute top-[1px] w-[1px] h-[calc(100%-2px)] left-[33.575%] bg-[var(--border-color)]"></div>
          <div class="w-full h-[1px] relative overflow-hidden"><div class="h-full w-full absolute top-0 left-0 bg-[var(--border-color)]"></div></div>
  
          <div class="grid grid-cols-12 grid-rows-1 gap-8 py-[5vw]">
              <!-- *Description -->
              <div class="col-span-4 pr-24">
                  <div class="flex flex-col justify-between gap-y-[10vw]">
                      <div>
                          <div class="inline-block uppercase rounded-[999px] border mb-4 px-6 py-[0.75rem] font-bold trackint-[0.033rem] text-[var(--small-size)]">Explore</div>
                          <div class="font-[Montserrat_Variable] text-[clamp(32px,5vw,128px)] leading-[0.825] tracking-[-.02em] uppercase my-0">Explore Crafts</div>
                          <p class="my-10 mx-0 text-[clamp(14px,0.938vw,24px)] opacity-70">Our unique approach to creativity means that the worlds we build transcend the media they inhabit. </p>
                      </div>
  
                      <div class="flex items-center">
                          <button 
                              class="flex items-center bg-transparent rounded-[999px] border-1 px-[1.5em] py-[1em]" 
                              aria-label="Previous"
                              on:click={prevBtn}
                          >
                              <svg width="43" height="19" viewBox="0 0 43 19" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8.73267 17.4646L1.00035 9.73228L8.73266 1.99996" stroke="white" stroke-width="2" stroke-miterlimit="10" stroke-linecap="square" stroke-linejoin="bevel"></path><path d="M41.0601 10.1072L1.81897 9.81861" stroke="white" stroke-width="2" stroke-miterlimit="10" stroke-linecap="square" stroke-linejoin="round"></path></svg>
                          </button>
                          <button 
                              class="flex items-center bg-transparent rounded-[999px] border-1 px-[1.5em] py-[1rem] ml-[2.5rem]" 
                              aria-label="Next"
                              on:click={nextBtn}
                          >
                              <svg width="43" height="19" viewBox="0 0 43 19" fill="none" xmlns="http://www.w3.org/2000/svg" class="rotate-180"><path d="M8.73267 17.4646L1.00035 9.73228L8.73266 1.99996" stroke="white" stroke-width="2" stroke-miterlimit="10" stroke-linecap="square" stroke-linejoin="bevel"></path><path d="M41.0601 10.1072L1.81897 9.81861" stroke="white" stroke-width="2" stroke-miterlimit="10" stroke-linecap="square" stroke-linejoin="round"></path></svg>
                          </button>
                      </div>
                  </div>
              </div>
              
              <!-- *Contents -->
              <div class="col-span-8 col-start-5 pl-24 overflow-hidden">
                  <div class="relative w-full h-full">
                      <div 
                          class="flex py-4 -mx-4 px-4" 
                          bind:this={sliderContent}
                          style="will-change: transform;"
                      >
                          <!-- Slider items -->
                          <div class="flex-shrink-0 w-[300px] h-[400px] bg-gray-800 rounded-xl mx-4" bind:this={items[0]}><img class="size-full object-cover rounded-xl" src="images/builds/build_1.png" alt="builds"></div>
                          <div class="flex-shrink-0 w-[300px] h-[400px] bg-gray-700 rounded-xl mx-4" bind:this={items[1]}><img class="size-full object-cover rounded-xl" src="images/builds/build_2.png" alt="builds"></div>
                          <div class="flex-shrink-0 w-[300px] h-[400px] bg-gray-600 rounded-xl mx-4" bind:this={items[2]}><img class="size-full object-cover rounded-xl" src="images/builds/build_3.png" alt="builds"></div>
                          <div class="flex-shrink-0 w-[300px] h-[400px] bg-gray-500 rounded-xl mx-4" bind:this={items[3]}><img class="size-full object-cover rounded-xl" src="images/builds/build_4.png" alt="builds"></div>
                          <div class="flex-shrink-0 w-[300px] h-[400px] bg-gray-400 rounded-xl mx-4" bind:this={items[4]}><img class="size-full object-cover rounded-xl" src="images/builds/build_5.png" alt="builds"></div>
                          <div class="flex-shrink-0 w-[300px] h-[400px] bg-gray-300 rounded-xl mx-4" bind:this={items[5]}><img class="size-full object-cover rounded-xl" src="images/builds/build_6.png" alt="builds"></div>
                          <div class="flex-shrink-0 w-[300px] h-[400px] bg-gray-300 rounded-xl mx-4" bind:this={items[6]}><img class="size-full object-cover rounded-xl" src="images/builds/build_7.png" alt="builds"></div>
                      </div>
                  </div>
              </div>
          </div>
          
          <div class="w-full h-[1px] relative overflow-hidden"><div class="h-full w-full absolute top-0 left-0 bg-[var(--border-color)]"></div></div>
      </div>
  </section>