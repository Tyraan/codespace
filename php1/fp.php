<?php
/**
 * Created by PhpStorm.
 * Author: Tyraan
 * Date: 2014/12/17
 * Time: 15:51
 */

$word =$_POST['word'];
$number = $_POST['number'];
$chunks = ceil(strlen($word)/$number);
echo "The {$number}- letter chunks of {$word} are <br />\n";
for($i=0;$i<$chunks;$i++){
    $chunk = substr($word,$i*$number,$number);
    printf("%d: %s <br /> \n",$i+1,$chunk);
}
echo '$_GET';
var_dump($_GET);
echo'<br/><hr></hr>';
echo'$_SERVER';
var_dump($_SERVER);
echo'<br/><hr></hr>';
echo '$_POST';
var_dump($_POST);
echo'<br/><hr></hr>';
echo'$_FILES';
var_dump($_FILES);
echo'<br/><hr></hr>';
echo'$_COOKIE';
var_dump($_COOKIE);
echo '<br/><hr></hr>';
echo'$_ENV';
var_dump($_ENV);





















