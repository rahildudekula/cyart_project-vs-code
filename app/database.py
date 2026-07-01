from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self):
        # Hardcoded connection - NO .env needed
        self.uri = "bolt://localhost:7687"
        self.user = "neo4j"
        self.password = "Zara@143"   # Your password
        
        self.driver = GraphDatabase.driver(
            self.uri, 
            auth=(self.user, self.password)
        )
    
    def close(self):
        self.driver.close()
    
    def query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record.data() for record in result]


db = Neo4jConnection()