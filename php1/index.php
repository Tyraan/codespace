<?php
/**
 * Created by PhpStorm.
 * User: Tyraan
 * Date: 2014/12/30
 * Time: 13:35
 */
include ("MyTpl.class.php");
$date_default_timezone_set('Asia/shanghai');
$now = time();
$tpl->asaign('now':$now);
$tpl->display('index.html');

?>
<div id =  content >
    <p> 后台管理</p>
    <table>
        <tr>
            <th>
                商品编号
            </th>
            <th>名称</th>
            <th>价格</th>
            <th>时间</th>

        </tr>

<?php
/*
  * sql 语句
  */
//?>

    </table>
</div>

<div id = page >
    <?echo $page> /<? echo $pageend ?>
    <a href="?page=1">首页</a>
    <a href="?page= <?echo $page ==1 ?1:($page-1)?>">上一页</a>
    <a href="?page= <?echo $page ==1 ?1:($page+1)?>">下一页</a>
    <?php
$listnum = 4;
