<?php
/**
 * Created by PhpStorm.
 * User: Tyraan
 * Date: 2014/12/30
 * Time: 11:28
 */
include_once('../Smarty/Smarty.class.php');
class MyTpl extends Smarty{
    public function __construct(){
        require_once('config.inc.php');
        $this->template_dir = ROOT.TEMPLATE_DIR;
        $this->compile_dir = ROOT.COMPILE_DIR;
        $this->config_dir = ROOT.CONFIG_DIR;

    }
}
$tpl = new MyTpl()
    ?>