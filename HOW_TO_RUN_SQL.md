# Getting Started

OPEN, **MySQL Command Line Client**

## How to use MySQL Command Line Client

command-line client, open the program and enter the password. After that, you will be able to use the client.

Use MySQL command line
You can also access MySQL Command Line Client from Command Prompt. For this:

1. Open Command Prompt.
2. Navigate to the bin folder. For example: `cd C:\Program Files\MySQL\MySQL Server 8.0\bin`
3. Run the `mysql -u root -p` command.
4. Enter the password.


## How to start managing MySQL database from the command line

First of all, we need to create a user. For this, we run the following command:

`CREATE USER 'username' IDENTIFIED BY 'password';`

Don’t forget to replace the username and password placeholders with a username and password of your choice.

Keep in mind, that just creating a user is not enough, you need to grant certain privileges to this user. For this, run the MySQL query:

`GRANT SELECT ON *.* TO 'username';`

This explicitly grants only the SELECT permission for the specified user. In case you want to grant a user all permissions on all databases, run the following command:

`GRANT ALL PRIVILEGES ON *.* TO 'username';.`

MySQL command line tools - grant user permissions
For more information, please refer to How to create a new user in MySQL.

## How to create a database from the command line

To create a database, use the following command. Replace the placeholder with the required name of the database.

`CREATE DATABASE dbname; `

To start working with the newly created database, execute the query:

`USE dbname;`

MySQL command line syntax - create a database
