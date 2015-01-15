<?php
/**
 * Created by PhpStorm.
 * User: Tyraan
 * Date: 2015/1/9
 * Time: 10:56
 */
$hello= "hello here is a php";
$hi = array();
var_dump($hello);
$output = shell_exec('python caughtByPhp.py here is something ');
var_dump($output);
echo "this is output by exec";
echo exec("python caughtByPhp.py  here is something ",$hi,$hello);
var_dump($hi);
var_dump($hello);