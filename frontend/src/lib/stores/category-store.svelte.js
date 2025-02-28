export const CategoryStore = $state([
    {name:'cpu', title: 'Processors', subTitle:'The heart of the machine', description:'The processor defines how fast the PC will be. The amount of cores, their clock and IPC are important.'},
    {name:'gpu', title: 'Graphics Card', subTitle:'Defining performance in games', description:'A strong graphics card is important for performance in games and in tasks like Machine Learning.'},
    {name:'memory', title: 'Memory', subTitle:'When more is more', description:'RAM holds all the data programs need to function. Without enough ram the PC will be very slow.'},
    {name:'motherboard', title: 'Motherboards', subTitle:'Where everything connects', description:'The motherboard holds the other components. Primarily its socket needs to fit to the processor.'},
    {name:'ssd', title: 'Solid State Drives', subTitle:'For programs you use often', description:'Modern SSDs provide fast access to data, improving system responsiveness.'},
    {name:'hdd', title: 'Hard Drives', subTitle:'Cold storage', description:'Classic hard disks are a good solution to store data that is not regularly needed.'},
    {name:'psu', title: 'Power Supplies', subTitle:'It won\'t work without energy', description:'Translating electricity to the voltage needed by other components.'},
    {name:'cooler', title: 'Coolers', subTitle:'Cool and quiet', description:'Air or AIO water cooler are supposed to cool the processor quietly and efficiently.'},
    {name:'case', title: 'Cases', subTitle:'The outer shell', description:'Good cases make building the PC easier, provide enough air flow and look nice.'},
    {name:'monitor', title: 'Monitors', subTitle:'Your window into this world', description:'Monitors vary a lot, with different resolutions, refresh rates and panel technologies.'},
]);