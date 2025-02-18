<script>
    /** @type {{ data: import('./$types').PageData }} */
    // let { data } = $props();

    import data from './data.json';
  
  let searchQuery = '';

  // Filter components based on search query
  $: filteredComponents = data.filter(component =>
    component.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    component.type.toLowerCase().includes(searchQuery.toLowerCase())
  );
</script>

<div class="container">
    <div class="search-bar">
        <input
            type="text"
            placeholder="Search components..."
            bind:value={searchQuery}
        />
    </div>
  
    <div class="cards">
        {#each filteredComponents as component}
            <div class="card">
                <h2>{component.name}</h2>
                <p><strong>Type:</strong> {component.type}</p>
                <p><strong>Price:</strong> <span class="price">{component.price}</span></p>
                <p>{component.description}</p>
            </div>
        {/each}
    </div>
</div>


  <style>
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
    }
  
    .search-bar {
      margin-bottom: 20px;
    }
  
    .search-bar input {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
  
    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 20px;
    }
  
    .card {
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 20px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
  
    .card h2 {
      margin: 0 0 10px;
      font-size: 24px;
    }
  
    .card p {
      margin: 5px 0;
      color: #555;
    }
  
    .card .price {
      font-weight: bold;
      color: #000;
    }
</style>