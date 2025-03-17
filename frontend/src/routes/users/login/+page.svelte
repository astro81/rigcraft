<script>
    let username = ''
    let password = ''
    let errors = {}
</script>

<section class="w-screen h-screen flex justify-center items-center">
    <div class="outline-1 flex flex-col justify-center items-center p-4">
        <h1 class="text-2xl font-medium">Login</h1>

        <form class="flex flex-col justify-center items-center gap-4 m-4">

            <div class="outline-1">
                <input type="text" placeholder="username" bind:value={username} />
            </div>
            <div class="outline-1">
                <input type="password" placeholder="password" bind:value={password} />
            </div>  

            <button type="submit" class="outline-1 rounded-[4px] px-3 py-1">Login</button>
        </form>
    </div>
</section>