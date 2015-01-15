<?php
/**
 * Created by PhpStorm.
 * Author: Tyraan
 * Date: 2014/12/22
 * Time: 10:26
 * 构建一个DataBaseHandler 类来处理常见的php数据库增删改查操作，
 * 类实力初始化时 分别需要$DBHost（服务器名称,$userName（用户名）,
 * $passWord（密码）,$DBname（数据库名，默认为空）,$tableName=''(表名称，默认为空)
 * connect方法连接数据库，其他方法内有均自动连接数据库。
 * 所有方法在失败时均返回false
 * 该类实例 有set/getTableName方法用于获得或改变当前的表名
 * set/getDBName 用于获得或改变当前数据库
 * insert 方法 用于向表中加入内容
 * select 和selectAll 方法，返回向数据库查询的内容
 * update 方法，用于向表中改动数据。
 * delete 方法，用于删除表中内容。
 */

class DataBaseHandler{
    public $dbHost;
    public $userName;
    public $password;
    public $dbName;
    private $db;
    private $prepareObj;
    /*
     * 类初始函数
     * 输入$DBHost（服务器名称,$userName（用户名）, * $passWord（密码）,$DBName（数据库名，默认为空）,$tableName=''(表名称，默认为空)
     * return 类实例
     * */
    public function __construct($dbHost,$userName,$password,$dbName){
        $this->dbHost    = $dbHost;
        $this->userName  = $userName;
        $this->password  = $password;
        $this->dbName     = $dbName;
        $this->db         = null;
        $this->prepareObj  = null;
    }
    public function getDBName(){
        return $this->dbName;
    }
    /*在数据中创建表，
    成功则返回true
     */
    /*先用$queryString代替 查询字符串处理对象。*/

    public function connect(){
        try {
            $this->db = new PDO("mysql:host={$this->dbHost};dbname = {$this->dbName}", $this->userName, $this->password);
            $this->db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        }catch (Exception $someerror){
            die('connection failed '.$someerror->getMessage());
        }
    }
    public function createTable($queryString){
        try {
            $this->db->exec($queryString);
        }catch (Exception $someerror){
            die('creatnew table failed '.$someerror->getMessage());
        }
    }


    /**
     * 向表中插入数据
     * @param $queryString  查询参数类型
     * @return
     */
    public function insert($queryString){
        try {
            $this->db->exec($queryString);
        }catch (Exception $someerror){
            die('connection failed '.$someerror->getMessage());
        }
    }
    /*select 向数据库查询数据
         第一个参数为条目名称，第二个参数为mysql条件语句
        返回查询结果
     * */
    public function select($queryString){
        try {
            $result = $this->db->query($queryString);
            $this -> echoResult($result);
        }catch (Exception $someerror){
            die('connection failed '.$someerror->getMessage());
        }

    }

    /*修改表中的数据
    输入 目标的条目集合，以及查询条件，
    返回结果。 ，
     * */
    public function update($queryString){
        try {
            $result = $this->db->query($queryString);
            $this -> echoResult($result);
        }catch (Exception $someerror){
            die('connection failed '.$someerror->getMessage());
        }

    }

    /*删除表中的数据。
    返回结果。
     * */
    public function  delete($queryString){
        try {
            $this->db->exec($queryString);
        }catch (Exception $someerror){
            die('connection failed '.$someerror->getMessage());
        }

    }
    public function echoResult($result){
        echo"fetch resul";
        while($row = $result->fetch()){
            print_r($row);
            }
        }

    public function closeDb(){
        $this->db = null;
    }

}

class MysqlString{
    public $deleteString;
    public $updateString;
    public $insertString;
    public $valueString;
    public $selectString;
    public $tableName;
    public function __construct($tableName){
        $this -> tableName=$tableName;
        $this -> updateString='';
        $this->insertString = '';
        $this->valueString = '';
        $this-> deleteString = '';
        $this-> selectString = '';
    }
    public function setTableName($newName){
        $this->tableName = $newName;
    }

}