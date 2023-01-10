from gettext import find
from turtle import update
from neo4j import GraphDatabase

uri = "bolt:http//localhost:7687"
userName = "[User]"
password = "[Pass]"

graphDB_Driver = GraphDatabase.driver(uri, auth=(userName, password))

#CRUD Functions
findPerson = "MATCH (n) where n.EmployeeId = '10000' RETURN n"
deletePerson = "MATCH (n) where n.EmployeeId = '10000' DETACH DELETE n"
createPerson = """
    create (n:Employee {
    EmployeeId: '10000',
    FirstName: 'LUCY',
    LastName: 'DALE',
    HireYear: '2013'})"""

updatePerson = """
    MATCH (p:Employee {FirstName:'LUCY'})
    SET p.isWorking ='Working'
    RETURN p"""

#lab doc
q1 = "match (n) where ID(n) = 10004 return n"
q2 = "MATCH (n:Employee) WHERE n.HireYear CONTAINS '20' RETURN n.FirstName"
q3 = "MATCH p=()-[r:FRIENDS_WITH]->() RETURN p"
q4 = "MATCH (n) WHERE n.isWorking is not null RETURN n"
q5 = "MATCH (n) WHERE n.isWorking is null RETURN n"
q6 = "MATCH (n:Employee) WHERE n.isWorking is not null RETURN COUNT(n) "

with graphDB_Driver.session() as graphDB_Session:
    nodes = graphDB_Session.run(updatePerson)
    for node in nodes:
        print(node)