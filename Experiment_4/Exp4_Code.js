// EXPERIMENT 4 — run using mongosh
// Database and collection
use online_book_store
if (!db.getCollectionNames().includes("books")) {
  db.createCollection("books")
}
show collections

// INSERT ONE
db.books.insertOne({
  book_id: 101,
  title: "The Alchemist",
  author: "Paulo Coelho",
  category: "Fiction",
  price: 350,
  stock: 20
})

// INSERT MANY
db.books.insertMany([
  { book_id: 102, title: "Atomic Habits", author: "James Clear", category: "Self Help", price: 499, stock: 15 },
  { book_id: 103, title: "Clean Code", author: "Robert C. Martin", category: "Programming", price: 650, stock: 10 },
  { book_id: 104, title: "Rich Dad Poor Dad", author: "Robert Kiyosaki", category: "Finance", price: 399, stock: 25 },
  { book_id: 105, title: "Introduction to Algorithms", author: "Thomas H. Cormen", category: "Programming", price: 850, stock: 8 }
])

// READ
db.books.find()
db.books.find().pretty()
db.books.findOne({ book_id: 103 })
db.books.find({ category: "Programming" })
db.books.find({ price: { $gt: 500 } })

// UPDATE ONE + VERIFY
db.books.updateOne(
  { book_id: 101 },
  { $set: { price: 375 } }
)
db.books.findOne({ book_id: 101 })

// UPDATE MANY: increase price of Programming books by 10%
db.books.updateMany(
  { category: "Programming" },
  { $mul: { price: 1.10 } }
)
db.books.find({ category: "Programming" })

// DELETE ONE + VERIFY
db.books.deleteOne({ book_id: 104 })
db.books.find()

// FIND / SEARCH
db.books.find({ price: { $gte: 400 } }).pretty()

// Title contains "Code" (case-insensitive)
db.books.find({ title: { $regex: "Code", $options: "i" } })

// Titles starting with "The"
db.books.find({ title: { $regex: "^The", $options: "i" } })

// Programming books costing more than 500
db.books.find({
  $and: [
    { category: "Programming" },
    { price: { $gt: 500 } }
  ]
})

// OR condition: Fiction OR price below 400
db.books.find({
  $or: [
    { category: "Fiction" },
    { price: { $lt: 400 } }
  ]
})

// INDEXING
db.books.getIndexes()
db.books.createIndex({ title: 1 })
db.books.getIndexes()

// AGGREGATION with $match
db.books.aggregate([
  { $match: { category: "Programming" } }
])

// $match + $sort
db.books.aggregate([
  { $match: { category: "Programming" } },
  { $sort: { price: -1 } }
])

// COMPOUND INDEX: category ascending, price ascending
db.books.createIndex({ category: 1, price: 1 })
db.books.getIndexes()

// Final display
db.books.find().pretty()
