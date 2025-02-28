/** @type {import('./$types.js').PageLoad} */
export async function load({ params }) {
    return {
        name: params.component_name
    };
};