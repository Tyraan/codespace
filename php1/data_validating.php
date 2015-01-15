<?php
/**
 * Created by PhpStorm.
 * User: Tyraan
 * Date: 2014/12/29
 * Time: 14:54
 */
$name = $_POST['name'];
$mediaType = $_POST['mediaType'];
$filename  = $_POST['filename'];
$caption   = $_POST['caption'];
$status    = $_POST['status'];
$tried    = ($_POST['tried'] == 'yes');
if($tried){
    $validated = (!empty($name) && !empty($mediaType) && !empty($filename));
    if(!$validated){
        ?>
        <p> username ,mediatype and filenmae require field ,fill them out to continue</p>
    <?php
    }
}
if ($tried && $validated){
    echo '<p>the item has been created</p>';
}
function mediaSelect($type)
{
    global $mediaType;

    if ($mediaType == $type){
        echo "selected";    }
}?>

<form action="<?php echo $_SERVER[ 'PHP_SELF']; ?>" method="POST">

    Name <input type="text" name="name" value="<?=$name;?>"/><br/>

    Status :<input type="checkbox" name="status" value="active"
        <?php if ($status=='active'){ echo "checked";} ?> />Active <br />

    Media :<select name ='mediaType' >
        <option value="">Choose one type of your file </option>
        <option value="picture" <?php mediaSelect('picture');?> />Picture</option>
        <option value="audio" <?php mediaSelect('audio');?> />audio</option>
        <option value="text" <?php mediaSelect('text');?> />text</option>
        </select>

    File <input type="text" name="filename"  value ="<?=$filename; ?>" /><br/>

    Caption :<textarea name = 'caption'><?=$caption;?></textarea><br />

    <input type="hidden" name = 'tried' value="yes"/>
    <input type="submit" name="<?php echo $tried ? "Continue":"Create";?>"/>
</form>