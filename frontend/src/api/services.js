import api from './axios';

export const getPlayers = (search = '') => {
  return api.get(`/players/${search ? `?search=${search}` : ''}`);
};

export const getTeams = (search = '') => {
  return api.get(`/teams/${search ? `?search=${search}` : ''}`);
};

export const getMyEvents = () => {
  return api.get('/games/my_events/');
};

export const getFavorites = () => {
  return api.get('/favorites/');
};

export const addFavorite = (data) => {
  return api.post('/favorites/', data);
};

export const deleteFavorite = (id) => {
  return api.delete(`/favorites/${id}/`);
};