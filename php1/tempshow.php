<html>
<head><title>Temperature conversion </title>
    /**
    * Created by PhpStorm.
    * User: Tyraan
    * Date: 2014/12/25
    * Time: 14:38
    */
</head>
<body>
<?php if($_SERVER['REQUEST_METHOD']=='GET'){ ?>
    <form action="<?php echo $_SERVER['PHP_SELF'] ?>" method="POST">
        Fahrenheit temperature:
    <input type ="text" name = 'fahrenheit'/><br/>
        <input type="submit" value="celsius fy">
     </form>
<?php }
else if($_SERVER['REQUEST_METHOD']=='POST'){
    $fahrentheit = $_POST['fahrenheit'];
    $celsius = ($fahrentheit - 32)*5/9;
    printf("%.2fF is %.2fC",$fahrentheit,$celsius);
}else{
    die("only work with get or post requests.");
}?>
<?php
    echo "<br/><hr></hr>";
    echo date("y-m-d h:i:s \n",time());
    echo "servertime is \n";
    echo  $_server['server_time'];
echo "<br/><hr></hr>";
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
?>
</body>
</html>