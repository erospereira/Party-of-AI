const { MongoClient } = require('mongodb');

async function run() {
  const client = new MongoClient("mongodb://localhost:27017/");

  try {
    await client.connect();
    const db = client.db("CALGARY");  // Replace with your database name
    const collection = db.collection("Statistics");  // Replace with your collection name

    const data = await collection.find().toArray();
    console.log(data);
  } finally {
    await client.close();
  }
}

run().catch(console.dir);
