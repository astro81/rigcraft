<script>
	import { goto } from "$app/navigation";
	import { preventDefault } from "svelte/legacy";

    let username = ''
    let password = ''
    let errors = {}

    let handleSubmit = async () => {
        const endpoint = 'http://127.0.0.1:8000/user/register/';
        const requestOptions = {
            method: 'POST',
            headers: {'Content-Type': 'application/json',},
            body: JSON.stringify({ username: username, password: password }),
        };
        // fetch(endpoint, requestOptions)
        //     .then(response => response.json().then(data => ({status: response.status, body: data})))
        //     .then(data => {
        //         if (data.status === 201) {
        //             goto('/user/login');
        //             // todo: display success popup
        //         } else {
        //             errors = data.body;
        //             // console.log(data);
        //             console.log('Error:', errors);
        //         }
        //     })

        try {
			const response = await fetch(endpoint, requestOptions);
			const data = await response.json();

			if (response.status === 201) {
				// Redirect to login page on successful registration
				goto('/user/login');
				// todo: display success popup
			} else {
				// Display errors from the backend
				errors = data;
				console.log('Error:', errors);
			}
		} catch (error) {
			console.error('Fetch error:', error);
		}

    }
</script>

<section class="w-screen h-screen flex justify-center items-center">
    <div class="outline-1 flex flex-col justify-center items-center p-4">
        <h1 class="text-2xl font-medium">Register</h1>

        <form 
            class="flex flex-col justify-center items-center gap-4 m-4"
            onsubmit={preventDefault(handleSubmit)}
            >

            <div class="outline-1">
                <input type="text" placeholder="username" bind:value={username} />
                {#if errors && errors.username }
                    <p class="text-red-500">{errors.username[0]}</p>
                {/if}
            </div>
            <div class="outline-1">
                <input type="password" placeholder="password" bind:value={password} />
                {#if errors && errors.password }
                    <p class="text-red-500">{errors.password[0]}</p>
                {/if}
            </div>  

            <button type="submit" class="outline-1 rounded-[4px] px-3 py-1frontend/src/routes/users/register/+page.svelte">Register</button>
        </form>
    </div>
</section>