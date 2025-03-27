// component-api.js
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL + '/api';

// Component type configuration
export const componentTypeMap = {
    cpu: {
        endpoint: 'components/cpu',
        displayFields: [
            { key: 'component_cpu_name', label: 'Name' },
            { key: 'component_cpu_cores', label: 'Cores' },
            { key: 'component_cpu_clock_speed', label: 'Clock Speed (GHz)' },
            { key: 'component_cpu_threads', label: 'Threads' },
            { key: 'component_cpu_price', label: 'Price ($)' }
        ],
        imageField: 'component_cpu_image',
        idField: 'component_cpu_id',
        nameField: 'component_cpu_name'
    },
    memory: {
        endpoint: 'components/memory',
        displayFields: [
            { key: 'component_memory_name', label: 'Name' },
            { key: 'component_memory_type', label: 'Type' },
            { key: 'component_memory_size', label: 'Size (GB)' },
            { key: 'component_memory_clock_speed', label: 'Clock Speed (MHz)' },
            { key: 'component_memory_price', label: 'Price ($)' }
        ],
        imageField: 'component_memory_image',
        idField: 'component_memory_id',
        nameField: 'component_memory_name'
    },
    gpu: {
        endpoint: 'components/gpu',
        displayFields: [
            { key: 'component_gpu_name', label: 'Name' },
            { key: 'component_gpu_vram', label: 'VRAM (GB)' },
            { key: 'component_gpu_boost_clock', label: 'Boost Clock (MHz)' },
            { key: 'component_gpu_power_consumption', label: 'Power (W)' },
            { key: 'component_gpu_price', label: 'Price ($)' }
        ],
        imageField: 'component_gpu_image',
        idField: 'component_gpu_id',
        nameField: 'component_gpu_name'
    }
};

// Fetch components of a specific type
export async function fetchComponents(type) {
    if (!componentTypeMap[type]) {
        throw new Error(`Invalid component type: ${type}`);
    }
    
    const response = await axios.get(`${API_BASE_URL}/${componentTypeMap[type].endpoint}/`);
    return response.data;

}

// Fetch a specific component by type and name
export async function fetchComponentDetail(type, name) {
    if (!componentTypeMap[type]) {
        throw new Error(`Invalid component type: ${type}`);
    }
    
    const response = await axios.get(`${API_BASE_URL}/${componentTypeMap[type].endpoint}/${encodeURIComponent(name)}/`);
    return response.data;
}

