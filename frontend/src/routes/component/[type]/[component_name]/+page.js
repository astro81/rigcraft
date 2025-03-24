/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
    return {
        component_type: params.type,
        component_name: params.component_name,
    };
};