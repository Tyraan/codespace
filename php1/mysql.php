<?php
/**
 * Created by PhpStorm.
 * User: Tyraan
 * Date: 2014/12/25
 * Time: 13:31
 */$columnQuery = array("BookName varchar(128)","PublicDate datetime","Price decimal(8,2)","Author tinytext");
$host='10.5.10.19';
$username = 'root';
$password = '123456';
$dbname = 'Books';
echo"mysql:host={$host};dbname = {$dbname}";
$dbobj = new PDO("mysql:host={$host};dbname = {$dbname}",$username,$password,array(PDO_ATTR_PERSISTENT=>true));
$dbobj->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_OBJ);
$queryString = implode(' ',$columnQuery);
$str= "CREATE TABLE {$queryString}";
echo $str;
$var_reply =$dbobj->exec("CREATE TABLE {$queryString}");
var_dump($var_reply);
$var_reply = $dbobj->exec("INSERT INTO Books (BookName PublicDate Price Author )VALUES('PHP Programming' '2013-12-10' 69 'Kevin Tatroe')");
var_dump($var_reply);
$dbobj = null;
