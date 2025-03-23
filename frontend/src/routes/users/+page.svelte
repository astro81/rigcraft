<script>
    import UserActionHead from "./UserActionHead.svelte";
    import LoginForm from "./LoginForm.svelte";
    import RegisterForm from "./RegisterForm.svelte";

    let isLoginFormVisible = $state(true);

    function toggleForm() {
        isLoginFormVisible = !isLoginFormVisible;
    }
</script>

<section class="flex justify-center items-center h-screen w-screen">
    <div class="relative w-[430px] rounded-[15px] px-8 pt-[120px] pb-16 border border-[var(--border-color)] shadow-lg transition-all duration-300 overflow-hidden" 
        style:height={isLoginFormVisible ? '500px' : '780px'}
        >

        <!-- Form Header -->
        <UserActionHead {isLoginFormVisible}/>

        <!-- LOGIN FORM -->
        <div class="absolute w-[85%] transition-all duration-300"
            style:left={isLoginFormVisible ? '50%' : '-50%'} 
            style:opacity={isLoginFormVisible ? 1 : 0}
            style:transform="translateX(-50%)">
            <LoginForm toggleForm={toggleForm} />
        </div>

        <!-- REGISTER FORM -->
        <div class="absolute w-[85%] transition-all duration-300"
            style:left={isLoginFormVisible ? '150%' : '50%'} 
            style:opacity={isLoginFormVisible ? 0 : 1}
            style:transform="translateX(-50%)">
            <RegisterForm toggleForm={toggleForm} />
        </div>
    </div>
</section>