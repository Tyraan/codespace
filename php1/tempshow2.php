<html>
<head><title>
        </title>
</head>
<body>
<?php
/**
 * Created by PhpStorm.
 * User: Tyraan
 * Date: 2014/12/25
 * Time: 15:20
 */
    $fahrenheit = $_GET['fahrenheit'];
    if(is_null($fahrenheit)){?>
    <form action="<?php echo $_SERVER['PHP_SELF'];?>" method="GET">
        Fahrenheti temperature:
        <input type="text" name ='fahrenheit'/><br/>
        <input type="submit" value="Convert"/><br/>
    </form>
<?php }else{
    $celsius = ($fahrenheit-32)*5/9;
    printf("%.2fF is %.2fC",$fahrentheit,$celsius);}
?>
}else{
    die("only work with get or post requests.");}
</body>
</html>