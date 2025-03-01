<script>
    let category = $props();
</script>

<div class="card border-2 m-4">
    <div class="flex flex-col justify-center items-start p-6 gap-y-8">
        <div>
            <h1 class="text-3xl font-semibold">{category.component_category_title}</h1>
            <h2 class="text-2xl font-medium">{category.component_category_sub_title}</h2>
        </div>
        <div>
            <p class="text-[1.1rem] opacity-70">{category.component_category_description}</p>
        </div>
        <div>
            <a href="components/{category.component_category_name}" class="block">
                <div class="button-box border-1 py-2 px-4 relative overflow-hidden">
                    <div class="text-[1.1rem] font-medium relative mix-blend-difference">
                        {category.component_category_name}
                    </div>
                </div>
            </a>
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