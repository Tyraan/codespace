<html>
<head><title></title></head>
<body>
<?php
/**
 * Created by PhpStorm.
 * User: Tyraan
 * Date: 2014/12/25
 * Time: 15:40
 */
$fah = $_GET['fah'];?>
<form action="<?php echo$_SERVER['PHP_SELF'];?>" method="GET">
    fah tem
    <input type = 'text' name = 'fah' value="<?php echo $fah;?>" /><br />
    <input type="submit" value  ="Convert"/>
    </form>
 <?php
 if(!is_null($fah)){
    $cel = $fah-32*5/9;
    printf("%.2f F is %.2f C",$fah,$cel);
    echo "<br/><hr>";
    echo date('Y-m-d H:i:s',$_SERVER['REQUEST_TIME']);
 }
 ?>
<form action="<?php echo $_SERVER['PHP_SELF'];?>" method="GET">
    Select you personality attributes :<br />
    <input type="checkbox" name="attributes[]" value="perky" checked />perky</br>
    <input type="checkbox" name="attributes[]" value="fucky" />fucky</br>
    <input type="checkbox" name="attributes[]" value="tkinky" />tkinky</br>
    <input type="checkbox" name="attributes[]" value="thrifty" />thrifty</br>
    <input type="checkbox" name="attributes[]" value="shopper" />shopper</br>
    <input type="checkbox" name="attributes[]" value="feeling" />feeling</br>
    <br />
    <input type="submit" name = 's' value="record personality">
</form>

<form enctype="multipart/form-data" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
    <input type="hidden" name="MAX_FILE_SIZE" value="10240">
    File name :<input name = 'toProcess' type="file">
    <input type="submit" value = "Upload"/>
</form>
<?php if(array_key_exists('s',$_GET)){
    $description =join(' ',$_GET['attributes']);
    echo "you have a {$description} personality";
}
if(is_uploaded_file($_FILES['toProcess']['tmp_name'])){
    move_uploaded_file($_FILES['toProcess']['tmp_name'],"{$_SERVER['DOCUMENT_ROOT']}/{$_FILES['toProcess']['name']}");
}


echo "<br/><hr>";
echo "servertime is \n";
echo date("y-m-d h:i:s \n",$_server['server_time']);
echo "<br/><hr>";
echo '$_GET';
var_dump($_GET);
echo'<br/><hr>';
echo'$_SERVER';
var_dump($_SERVER);
echo'<br/><hr>';
echo '$_POST';
var_dump($_POST);
echo'<br/><hr>';
echo'$_FILES';
var_dump($_FILES);
echo'<br/><hr>';
echo'$_COOKIE';
var_dump($_COOKIE);
echo '<br/><hr>';
echo'$_ENV';
var_dump($_ENV);
?>
</body>
</html>
