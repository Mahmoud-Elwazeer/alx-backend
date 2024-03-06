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

function publishMessage(message, time) {
  setTimeout(() => {
    client.publish('holberton school channel', message);
    console.log(`About to send ${message}`);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
