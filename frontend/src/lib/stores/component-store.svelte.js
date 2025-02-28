import cpu_data from './cpu-data.json';

// export const ComponentCpuStore = $state([
//     {id: 1, name: 'Ryzen 5', type: 'cpu'},
//     {id: 2, name: 'Corsair Vengence', type: 'memory'},
// ]);

export const ComponentCpuStore = $state(cpu_data);

console.log(cpu_data[0]);