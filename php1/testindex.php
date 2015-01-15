<?php
/**
 * Created by PhpStorm.
 * User: Tyraan
 * Date: 2014/12/24
 * Time: 15:06
 * MVC演示demo
 * 仅仅实现最基本的MVC功能，
 */
define('SITE_PATH',str_replace('','/',dirname(__FILE__)));//定义系统目录
$controller=(!empty($_GET['controller']))?$_GET['controller']:'index';//获取控制器,默认index
$action=(!empty($_GET['action']))?$_GET['action']:'index';//方法名称，默认index
$controller_name=$controller.'Controller';
$controller_file=SITE_PATH.'/app/controller/'.$controller_name.'.class.php';//获取控制器文件
if(file_exists($controller_file)){
    require_once($controller_file);
    $controller=new $controller_name();
    $controller->{$action.'Action'}();
}else{
    die('找不到对应的控制器！');
}

