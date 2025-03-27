// // $lib/stores/category-store.svelte.js

// export const componentCategoryStore = $state([]);

// $lib/stores/category-store.svelte.js
import { component_category } from '$lib/apis/category-api';

export const categories = $state([]);

export async function initializeCategories() {
    try {
        const fetchedCategories = await component_category();
        categories.splice(0, categories.length, ...fetchedCategories);
        return fetchedCategories;
    } catch (err) {
        console.error('Failed to fetch categories:', err);
        return [];
    }
}