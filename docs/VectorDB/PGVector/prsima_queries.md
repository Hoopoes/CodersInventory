# Postgres and Pg vector extension for enbaling Famous SQLDB to vector db
Prsima Guide for Python [Prisma Client Python](https://prisma-client-py.readthedocs.io/en/stable/)

- create prisma folder in root
- create .env file in prisma folder
`DATABASE_URL=postgresql://user_name:password@localhost:5432/database_name`

- add schema.prisma file in it
```prisma
generator client {
    provider             = "prisma-client-py"
    interface            = "sync"
    recursive_type_depth = 5
    previewFeatures = ["postgresqlExtensions"]
}


datasource db {
    provider    = "postgresql"
    url         = env("DATABASE_URL")
    extensions  = [pgvector(map: "vector", schema: "public")] 
}

model Image {
    p_id       Int         @id @default(autoincrement()) @map("_id")
    name       String?     @db.VarChar(20)
    embedding  Unsupported("vector(4096)")?     
    image      Bytes?
}

```
- run `prisma migrate dev --name "add_pgvector_extension"` or any other name in quotation.
- Then Convert embedding datatype to String? because due to unsupported yet, prisma would get error. (AS when data comes from dtabase, prisma faild to parse it)
```prisma
model Image {
    p_id       Int         @id @default(autoincrement()) @map("_id")
    name       String?     @db.VarChar(20)
    embedding  String?     
    image      Bytes?
}
```
- then run `prisma generate` and for any change in schema run `prisma generate`.


# Queries Database Using Prisma
```python
```py
from prisma import Prisma
prisma_client = Prisma()
```
As I have used `interface="sync"` in generator client in schema.prisma that's why i dont have to use aysnc/await but if i have used `asyncio` as interface then i would use async/await.
# Insert Query
```py
prisma_client.connect()


result = prisma_client.query_raw(
    query= \
f"""
INSERT INTO public.db (name, embedding) VALUES ('q', '[1,2,3,4]'), ('r', '[4,5,6,7]');
"""
    )

print(result) # empty string


prisma_client.disconnect()
```

Yes we need to use Raw Queries sadly as vector isnt supported yet

## Retrive Vector Query
```python
prisma_client.connect()


embedding_size = 4
result = prisma_client.query_raw(
    query= \
f"""
SELECT p_id, name, embedding::varchar({(embedding_size*2)+1}) FROM public.db WHERE db.name = 'umar'
"""
    )

for rec in result:
    rec['embedding'] = eval(rec['embedding']) # Eval to convert String to list
print(result)


prisma_client.disconnect()
```

Here I could Have get the embedding like `embedding::text` too without that varchar and embedding size and formula but this way it's keep the length check
```python
query= "SELECT p_id, name, embedding::text FROM public.db WHERE db.name = 'umar'"
    )
```

# Fetch using Cosine Similarity Without the Indexing
$$ 1 - cosine\ distance =\ \set{-1,1} $$
-1 to 1. -1 is opposite, 1 is similar. 

Need of subquery as cosine similarity distance is also fetch

```python
prisma_client.connect()


column = 'cosine_similarity'
result = prisma_client.query_raw(
    query= \
f"""
SELECT 
    name, 
    {column}  
FROM (
    SELECT 
        name, 
        1 - (embedding <=> '{[1,2,3,4]}') AS {column} 
    FROM db
) AS subquery
WHERE {column}  > {0.70}
ORDER BY cosine_similarity DESC
Limit {3};
"""
    )

print(result)


prisma_client.disconnect()
```

### No need of subquery but drawback
```sql
SELECT 
	name
FROM db
WHERE (1 - (embedding <=> '[1,2,3,4]')) > 0.70;
```
But here, no query way to like order them, yes we can put this like fetch by limit but no order by distance so subquery is needed