<script>
    let category = $props();
</script>

<div class="card border-2 m-4">
    <div class="flex flex-col justify-center items-start p-6 gap-y-8">
        
        <div>
            <h1 class="text-3xl font-semibold">{category.title}</h1>
            <h2 class="text-2xl font-medium">{category.subTitle}</h2>
        </div>
        <div>
            <p class="text-[1.1rem] opacity-70">{category.description}</p>
        </div>
        <div>
            <div class="button-box border-1 py-2 px-4 relative overflow-hidden">
                <a class="text-[1.1rem] font-medium relative mix-blend-difference" href="components/{category.name}">{category.name}</a>
            </div>
        </div>

    </div>
</div>

<style>
    .button-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: white;
        transform: translateX(-100%);
        transition: transform 0.3s ease;
    }

    .button-box:hover::before {
        transform: translateX(0);
    }
</style>