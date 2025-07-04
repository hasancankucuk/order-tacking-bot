const URL = process.env.REACT_APP_BACKEND_URL;

export const dropDatabase = async (api_url: string) => {
    try {
        const response = await fetch(`${process.env.REACT_APP_BACKEND_URL}/api/${api_url}`, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error updating user:', error);
    }
}


export const seedDb = async (role: string, api_url: string)=> {
    try {
        const response = await fetch(`${URL}/api/${api_url}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({role}),
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error updating user:', error);
    }
}