const API_BASE_URL = process.env.REACT_APP_BACKEND
console.log("API_BASE_URL:", process.env.REACT_APP_BACKEND);

export const fetchTokens = async () => {
  const response = await fetch(`${API_BASE_URL}/tokens/`);
  if (!response.ok) {
    throw new Error('Failed to fetch tokens');
  }
  return await response.json();
};

export const fetchPortfolio = async (params = {}) => {
  const queryString = new URLSearchParams(params).toString();
  const response = await fetch(`${API_BASE_URL}/portfolio/?${queryString}`);
  if (!response.ok) {
    throw new Error('Failed to fetch portfolio');
  }
  return await response.json();
};