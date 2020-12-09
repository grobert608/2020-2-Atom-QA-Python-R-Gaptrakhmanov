# Создание пользователя в базе

Для успешного прохождения тестов необходимо создать пользователя. Для этого:

$ sudo mysql -u root

MariaDB [(none)]> CREATE USER 'test_user'@localhost IDENTIFIED BY 'password';

MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'test_user'@localhost IDENTIFIED BY 'password';