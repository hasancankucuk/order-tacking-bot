const URL = process.env.REACT_APP_BACKEND_URL
export const updateUser = async (user: { id: number, username?: string, password?: string, email?: string, role?: string }, api_url: string) => {
    try {
        const response = await fetch(`${URL}/api/${api_url}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(user),
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

export const register = async (username: string, password: string, email: string, role: string, api_url: string) => {
    try {
        const response = await fetch(`${URL}/api/${api_url}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({username, password, email, role}),
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

export const login = async (username: string, password: string, api_url: string) => {
    try {
        const response = await fetch(`${URL}/api/${api_url}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password }),
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching custom query data:', error);
    }
}