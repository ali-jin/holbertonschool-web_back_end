import redis from 'redis';

const client = redis.createClient();

client.on('connect', function () {
  console.log('Redis client connected to the server');
});

client.on('error', function (error) {
  console.log(`Redis client not connected to the server: ${error}`);
});

const setHashValue = (hash, key, value) => {
  client.hset(hash, key, value, redis.print);
};

const displayHashValue = (hash) => {
  client.hgetall(hash, (error, value) => {
    if (error) throw error;
    console.log(value);
  });
};

setHashValue('HolbertonSchools', 'Portland', '50');
setHashValue('HolbertonSchools', 'Seattle', '80');
setHashValue('HolbertonSchools', 'New York', '20');
setHashValue('HolbertonSchools', 'Bogota', '20');
setHashValue('HolbertonSchools', 'Cali', '40');
setHashValue('HolbertonSchools', 'Paris', '2');

displayHashValue('HolbertonSchools');
