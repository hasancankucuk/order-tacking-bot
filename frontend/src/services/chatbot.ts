const RASA_URL = process.env.REACT_APP_RASA_URL;

export const postMessage = async (sessionId: string, message: string) => {
    try {
        const response = await fetch(`${RASA_URL}/webhooks/rest/webhook`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                sender: sessionId,
                message: message,
            }),
        });

        if (!response.ok) {
            console.log('Failed to post message:', response.statusText);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error posting message:', error);
    }
}

export const clearSession = async (sessionId: string) => {
    try {
        const response = await fetch(`${RASA_URL}/conversations/${sessionId}/tracker/events`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify([{ event: 'restart' }]),
        });

        if (!response.ok) {
            console.log('Failed to clear session:', response.statusText);
        }

        return response.ok;
    } catch (error) {
        console.error('Error clearing session:', error);
    }
}

export const listProducts = async (sessionId: string) => {
    try {
         const response = await fetch(`${RASA_URL}/webhooks/rest/webhook`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                sender: sessionId,
                message: "list products",
            }),
        });

        if (!response.ok) {
            console.log('Failed to fetch products:', response.statusText);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching products:', error);
    }
}