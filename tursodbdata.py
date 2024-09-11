import tursodb   
db = tursodb.connect("my_database")  
  
  
db.create_table("my_table", {  
    "id": tursodb.Integer,  
    "name": tursodb.String,  
    "age": tursodb.Integer  
})  
  
# Insert some data  
db.insert("my_table", [  
    {"id": 1, "name": "aditya", "age": 21},  
    {"id": 2, "name": "satyam", "age": 30},  
    {"id": 3, "name": "gopal", "age": 27}  
])  
  
# Query the data  
results = db.query("my_table", "SELECT * FROM my_table WHERE age > 30")  
for row in results:  
    print(row)  
   
db.close()