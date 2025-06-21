const URL = process.env.REACT_APP_BACKEND_URL
export const getTables = async () => {
    try {
        const response = await fetch(`${URL}/api/tables`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching tables:', error);
    }
};

export const getTableData = async (tableName: string) => {
    try {
        const response = await fetch(`${URL}/api/tables/${tableName}`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        if (data && typeof data === 'object' && tableName in data) {
            return data[tableName];
        }
        return data;
    } catch (error) {
        console.error('Error fetching table data:', error);
    }
}

export const customQuery = async (query: string) => {
    try {
        const response = await fetch(`${URL}/api/custom_query`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query }),
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching custom query data:', error);
    }
};

export const updateCustomQuery = async (query: string) => {
    try {
        const response = await fetch(`${URL}/api/custom_query`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query }),
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching custom query data:', error);
    }
};