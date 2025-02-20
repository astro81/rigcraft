<script>
  /** @type {{ data: import('./$types').PageData }} */
  // let { data } = $props();

  import data from './data.json';

  let searchQuery = $state('');
  let selectedType = $state('All');
  let selectedComponent = $state(null);
  let isModalOpen = $state(false);
  
  // Get unique component types
  let componentTypes = $derived(['All', ...new Set(data.map(component => component.type))]);
  
  let filteredComponents = $derived(
      data.filter(component => {
          const matchesSearch = 
              component.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
              component.description.toLowerCase().includes(searchQuery.toLowerCase());
          
          const matchesType = selectedType === 'All' || component.type === selectedType;
          
          return matchesSearch && matchesType;
      })
  );

  function getSpecHighlights(component) {
      switch (component.type) {
          case 'CPU':
              return `${component.specifications.cores} cores, ${component.specifications.boost_clock} boost`;
          case 'Memory':
              return `${component.specifications.memory_size} ${component.specifications.memory_type} @ ${component.specifications.speed}`;
          case 'SSD':
              return `${component.specifications.capacity} ${component.specifications.storage_type}`;
          case 'GPU':
              return `${component.specifications.memory.size} ${component.specifications.memory.type}`;
          case 'Motherboard':
              return `${component.specifications.socket}, ${component.specifications.chipset}`;
          default:
              return '';
      }
  }

  function openModal(component) {
      selectedComponent = component;
      isModalOpen = true;
  }

  function closeModal() {
      isModalOpen = false;
      selectedComponent = null;
  }

  // Close modal when clicking outside
  function handleModalClick(event) {
      if (event.target.classList.contains('modal-overlay')) {
          closeModal();
      }
  }

  // Format specifications object for display
  function formatSpecifications(specs, indent = 0) {
      if (typeof specs !== 'object' || specs === null) {
          return specs;
      }

      return Object.entries(specs).map(([key, value]) => {
          const formattedKey = key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
          if (typeof value === 'object' && value !== null) {
              return `
                  <div style="margin-left: ${indent}px">
                      <strong>${formattedKey}:</strong>
                      ${formatSpecifications(value, indent + 20)}
                  </div>
              `;
          }
          return `
              <div style="margin-left: ${indent}px">
                  <strong>${formattedKey}:</strong> ${value}
              </div>
          `;
      }).join('');
  }
</script>

<div class="container">
  <div class="filters">
      <div class="search-bar">
          <input
              type="text"
              placeholder="Search components..."
              bind:value={searchQuery}
          />
      </div>
      <div class="type-filter">
          <select bind:value={selectedType}>
              {#each componentTypes as type}
                  <option value={type}>{type}</option>
              {/each}
          </select>
      </div>
  </div>

  <div class="cards">
      {#each filteredComponents as component}
          <!-- svelte-ignore a11y_click_events_have_key_events -->
          <!-- svelte-ignore a11y_no_static_element_interactions -->
          <div class="card" onclick={() => openModal(component)}>
              <div class="card-header">
                  <span class="component-type">{component.type}</span>
                  <span class="price">{component.price}</span>
              </div>
              <h2>{component.name}</h2>
              <p class="specs">{getSpecHighlights(component)}</p>
              <p class="description">{component.description}</p>
          </div>
      {/each}
  </div>
</div>

{#if isModalOpen && selectedComponent}
  <!-- svelte-ignore a11y_click_events_have_key_events -->
  <!-- svelte-ignore a11y_no_static_element_interactions -->
  <div class="modal-overlay" onclick={handleModalClick}>
      <div class="modal">
          <div class="modal-header">
              <h2>{selectedComponent.name}</h2>
              <button class="close-button" onclick={closeModal}>&times;</button>
          </div>
          <div class="modal-content">
              <div class="modal-section">
                  <span class="component-type">{selectedComponent.type}</span>
                  <span class="price">{selectedComponent.price}</span>
              </div>
              <div class="modal-section">
                  <p class="description">{selectedComponent.description}</p>
              </div>
              <div class="modal-section specifications">
                  <h3>Specifications</h3>
                  {@html formatSpecifications(selectedComponent.specifications)}
              </div>
          </div>
      </div>
  </div>
{/if}

<style>
  .container {
      max-width: 1200px;
      margin: 12rem auto;
      padding: 20px;
  }

  .filters {
      display: flex;
      gap: 20px;
      margin-bottom: 30px;
  }

  .search-bar {
      flex: 1;
  }

  .search-bar input {
      width: 100%;
      padding: 12px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 5px;
  }

  .type-filter select {
      padding: 12px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 5px;
      min-width: 150px;
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
      /* background: white; */
      transition: transform 0.2s ease;
      cursor: pointer;
  }

  .card:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }

  .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
  }

  .component-type {
      /* background: #f0f0f0; */
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 18px;
      font-weight: 500;
      /* color: #666; */
  }

  .card h2 {
      margin: 0 0 10px;
      font-size: 20px;
      line-height: 1.3;
  }

  .specs {
      font-size: 14px;
      color: #666;
      margin: 10px 0;
  }

  .description {
      font-size: 14px;
      color: #444;
      line-height: 1.4;
  }

  .price {
      font-weight: bold;
      color: #2c5282;
      font-size: 18px;
  }

  /* Modal styles */
  .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.5);
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 1000;
  }

  .modal {
      background: white;
      border-radius: 8px;
      width: 90%;
      max-width: 800px;
      max-height: 90vh;
      overflow-y: auto;
      position: relative;
  }

  .modal-header {
      padding: 20px;
      border-bottom: 1px solid #eee;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      background: white;
      border-radius: 8px 8px 0 0;
  }

  .modal-header h2 {
      margin: 0;
      font-size: 24px;
  }

  .close-button {
      background: none;
      border: none;
      font-size: 28px;
      cursor: pointer;
      padding: 0 8px;
      color: #666;
  }

  .close-button:hover {
      color: #000;
  }

  .modal-content {
      padding: 20px;
  }

  .modal-section {
      margin-bottom: 20px;
  }

  .modal-section h3 {
      margin: 0 0 15px 0;
      font-size: 18px;
  }

  .specifications {
      font-size: 14px;
      line-height: 1.6;
  }

  .specifications div {
      margin-bottom: 8px;
  }
</style>