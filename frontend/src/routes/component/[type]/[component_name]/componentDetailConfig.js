// Detail view configurations for each component type
export const componentDetailConfig = {
    cpu: {
        displayGroups: [
            {
                title: 'Basic Information',
                fields: [
                    { key: 'component_cpu_brand', label: 'Brand' },
                    { key: 'component_cpu_series', label: 'Series' },
                    { key: 'component_cpu_model', label: 'Model' }
                ]
            },
            {
                title: 'Technical Specifications',
                fields: [
                    { key: 'component_cpu_socket', label: 'Socket' },
                    { key: 'component_cpu_clock_speed', label: 'Clock Speed (GHz)' },
                    { key: 'component_cpu_cores', label: 'Cores' },
                    { key: 'component_cpu_threads', label: 'Threads' }
                ]
            },
            {
                title: 'Purchase Information',
                fields: [
                    { key: 'component_cpu_price', label: 'Price ($)' }
                ]
            }
        ]
    },
    memory: {
        displayGroups: [
            {
                title: 'Basic Information',
                fields: [
                    { key: 'component_memory_producer', label: 'Producer' },
                    { key: 'component_memory_model', label: 'Model' }
                ]
            },
            {
                title: 'Technical Specifications',
                fields: [
                    { key: 'component_memory_type', label: 'Type' },
                    { key: 'component_memory_size', label: 'Size (GB)' },
                    { key: 'component_memory_clock_speed', label: 'Clock Speed (MHz)' }
                ]
            },
            {
                title: 'Purchase Information',
                fields: [
                    { key: 'component_memory_price', label: 'Price ($)' }
                ]
            }
        ]
    },
    gpu: {
        displayGroups: [
            {
                title: 'Basic Information',
                fields: [
                    { key: 'component_gpu_brand', label: 'Brand' },
                    { key: 'component_gpu_model', label: 'Model' },
                    { key: 'component_gpu_series', label: 'Series' }
                ]
            },
            {
                title: 'Technical Specifications',
                fields: [
                    { key: 'component_gpu_vram', label: 'VRAM (GB)' },
                    { key: 'component_gpu_boost_clock', label: 'Boost Clock (MHz)' },
                    { key: 'component_gpu_hdmi_port', label: 'HDMI Ports' },
                    { key: 'component_gpu_power_consumption', label: 'Power Consumption (W)' }
                ]
            },
            {
                title: 'Purchase Information',
                fields: [
                    { key: 'component_gpu_price', label: 'Price ($)' }
                ]
            }
        ]
    }
};