<!-- BuildCategorySelector -->
<script>
    let category = $props();
    let active = false;
</script>

<div class="mx-2 my-1">
    <div class="flex p-2">
        <div class="size-full">
            <div 
                class="button-box border-1 py-2 px-4 relative overflow-hidden"
                class:active-category={active}
            >
                <div class="text-[1.1rem] font-medium relative mix-blend-difference">
                    {category.component_category_title}
                </div>
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

    .active-category {
        background-color: rgba(0, 0, 0, 0.1);
        border-color: rgba(0, 0, 0, 0.2);
    }
</style>

