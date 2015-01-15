<?php
/**
 * Created by PhpStorm.
 * User: Tyraan
 * Date: 2014/12/24
 * Time: 16:49
 */
class loader
{
    private static $loaded = array();
    public static function load($object){
        $valid = array(
            "view",
            "model",
            "router",
            "config",
            "db");
        if (!in_array($object,$valid)){
            throw new Exception("Not a valid object '{$object}' to load");
        }
        if (empty(self::$loaded[$object])){
            self::$loaded[$object]= new $object();
        }
        return self::$loaded[$object];
    }
}