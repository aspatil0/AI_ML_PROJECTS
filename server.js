const express = require('express');
const  MongoClient = require('mongodb');
const port = 3099; 
const fs= require('fs')
const adi = express();



adi.listen(port, (err) => {
  if (err) {
    console.error(`Error starting server: ${err}`);
    process.exit(1);
  }
  console.log(`Server is running on port ${port}`);
});

adi.use(express.json());
const middleware =(req,res,next)=>{
    const date =new Date()
    fs.appendFile("./log.txt",`request from: ${date}`, (err)=>{
        console.log("error")
    });
    next();
}
adi.use(middleware);


adi.get('/', (req, res) => {
    console.log("dd0")
});

adi.get("/search",async (req,res)=>{
 
 const filter = {
  'name': 'aditya'
};
const client = await MongoClient.connect(
  'mongodb://localhost:27017/',
);
const coll = client.db('stud').collection('Student');
const cursor = coll.find(filter);
const result = await cursor.toArray();
await client.close();
res.json(result)
});