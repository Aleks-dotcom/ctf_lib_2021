const { unflatten } = require('flat');

const str = '{"artist.name": "nekaj"}'

console.log(unflatten(str))