<?php
/**
 * Created by PhpStorm.
 * User: Tyraan
 * Date: 2014/12/24
 * Time: 16:07
 */
set_include_path(get_include_path() . PATH_SEPARATOR ."core/main");
function __autoload($object){
    require_once("{$object}.php");
}
