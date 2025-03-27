// $lib/stores/build-store.svelte
import { writable } from 'svelte/store';

function createBuildStore() {
    const { subscribe, update, set } = writable({
        cpu: null,
        memory: null,
        gpu: null
    });

    return {
        subscribe,
        addComponent: (type, component) => update(store => ({
            ...store,
            [type]: component
        })),
        removeComponent: (type) => update(store => ({
            ...store,
            [type]: null
        })),
        reset: () => set({
            cpu: null,
            memory: null,
            gpu: null
        })
    };
}

export const buildStore = createBuildStore();
