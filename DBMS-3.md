
# TITLE :

MongoDB Queries:

Design and Develop MongoDB Queries using CRUD operations. (Use CRUD
operations, SAVE method, logical operator.



CODE:

Certainly! MongoDB uses CRUD operations (Create, Read, Update, Delete) for interacting with the database. Below are examples of MongoDB queries using these operations, the SAVE method, and logical operators:

### Create (Insert) Documents:

#### 1. Insert a Single Document:

```javascript

db.users.insertOne({
  name: "John Doe",
  age: 30,
  email: "john@example.com"
});

```

#### 2. Insert Multiple Documents:

```javascript

db.users.insertMany([
  {
    name: "Jane Doe",
    age: 25,
    email: "jane@example.com"
  },
  {
    name: "Bob Smith",
    age: 35,
    email: "bob@example.com"
  }
]);

```

### Read (Query) Documents:

#### 3. Find Documents:

```javascript

db.users.find({ age: { $gte: 30 } });

```

#### 4. Find Documents with Logical Operators:

```javascript

db.users.find({
  $or: [
    { age: { $gte: 30 } },
    { name: "Jane Doe" }
  ]
});

```

### Update Documents:

#### 5. Update a Single Document:

```javascript

db.users.updateOne(
  { name: "John Doe" },
  { $set: { age: 31 } }
);

```

#### 6. Update Multiple Documents:

```javascript

db.users.updateMany(
  { age: { $gte: 30 } },
  { $inc: { age: 1 } }
);

```

#### 7. Replace Document:

```javascript

db.users.replaceOne(
  { name: "Jane Doe" },
  { name: "Jane Smith", age: 26, email: "jane.smith@example.com" }
);

```

### Delete Documents:

#### 8. Delete a Single Document:

```javascript

db.users.deleteOne({ name: "Bob Smith" });

```

#### 9. Delete Multiple Documents:

```javascript

db.users.deleteMany({ age: { $lt: 30 } });

```

### SAVE Method:

#### 10. Using the SAVE Method:
Assuming you have a document with an "_id" field, the `save` method either updates an existing document or inserts a new one if the "_id" is not present:

```javascript

var userDocument = {
  _id: ObjectId("yourObjectId"),
  name: "Updated User",
  age: 32,
  email: "updated@example.com"
};

db.users.save(userDocument);

```

These MongoDB queries cover basic CRUD operations, logical operators in queries, and the SAVE method. Adjust these examples based on your MongoDB database structure and requirements.





