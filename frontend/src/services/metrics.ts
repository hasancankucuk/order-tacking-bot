const URL = process.env.REACT_APP_BACKEND_URL
export async function fetchNluTest() {
  try {
    const response = await fetch(`${URL}/api/test/nlu`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;

  } catch (error) {
    console.error("Error fetching NLU test:", error);
  }
}

export async function fetchCoreTest() {
  try {
    const response = await fetch(`${URL}/api/test/core`);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;

  } catch (error) {
    console.error("Error fetching core test:", error);
  }
}

export const fetchResults = (filename: string): string => {
  try {
    return `${URL}${filename.startsWith("/") ? filename : "/" + filename}`;
  } catch (error) {
    console.error("Error fetching results:", error);
    return "";
  }
};