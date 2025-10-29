import api from './axios';

// Example API service functions
// Uncomment and use these once you create the backend endpoints

// Player Services
export const playerService = {
  // Get all players
  getAll: () => api.get('/players/'),
  
  // Get single player
  getById: (id) => api.get(`/players/${id}/`),
  
  // Search players
  search: (query) => api.get('/players/', { params: { search: query } }),
};

// Game Services
export const gameService = {
  // Get all games
  getAll: () => api.get('/games/'),
  
  // Get single game
  getById: (id) => api.get(`/games/${id}/`),
  
  // Get upcoming games
  getUpcoming: () => api.get('/games/', { params: { status: 'upcoming' } }),
};

// Event Services
export const eventService = {
  // Get all events
  getAll: () => api.get('/events/'),
  
  // Get events for user's favorites
  getFavoriteEvents: () => api.get('/events/favorites/'),
};

// Favorite Services
export const favoriteService = {
  // Get user's favorites
  getAll: () => api.get('/favorites/'),
  
  // Add favorite
  add: (type, id) => api.post('/favorites/', { type, id }),
  
  // Remove favorite
  remove: (favoriteId) => api.delete(`/favorites/${favoriteId}/`),
};

// Auth Services
export const authService = {
  // Login
  login: (username, password) => 
    api.post('/auth/login/', { username, password }),
  
  // Logout
  logout: () => api.post('/auth/logout/'),
  
  // Register
  register: (userData) => api.post('/auth/register/', userData),
  
  // Get current user
  getCurrentUser: () => api.get('/auth/user/'),
};

export default {
  playerService,
  gameService,
  eventService,
  favoriteService,
  authService,
};

