/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
    return {
        component_type: params.type
    };
};