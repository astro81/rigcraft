/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
    return {
        buildId: params.build
    };
};