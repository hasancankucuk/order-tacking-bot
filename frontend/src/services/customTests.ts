const URL = process.env.REACT_APP_BACKEND_URL
export const runCustomNLUTest = async (text: string, expectedIntent: string) => {
        try {
        const response = await fetch(`${URL}/api/test/manuel/nlu`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text, expected_intent: expectedIntent }),
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