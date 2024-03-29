import { createClient } from 'redis'


// Create a Redis client
const client = createClient();

// Handling errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server')
});
