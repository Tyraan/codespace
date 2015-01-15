<?php
/**
 * Created by PhpStorm.
 * User: Tyraan
 * Date: 2014/12/17
 * Time: 10:41
 */

namespace devFR;


class UrlHandler{
    public $url;
    public $filename;

    /**
     *
     */
    public function __construct($url,$filename){
        $this->url=$url;
        $this->filename=$filename;
        //try{
        //打开url并下载到文件中。
        //$htmlContent=file_get_contents($url);
        //$htmlfile = fopen($filename,'w');
        //fwrite($htmlfile, $htmlContent);
        //fclose($htmlfile);

        //}catch(\Exception $error){
        //获取错误
        //    echo $error->getMessage();
        //}
    }

    /**
     *
     */
    public function parseContent(){
        try {
            if(file_exists($this->filename)) {
                $htmlContent = file_get_contents($this->url);
                file_put_contents($this->filename, $htmlContent);
            }else{
                $htmlContent = file_get_contents($this->filename);
            } //读取文件，按<分割，筛选有连接的元素，
            $htmlTextSplit = explode('"',$htmlContent);

            $hasLinks=array_filter($htmlTextSplit, array($this, 'filter'));
            var_dump($hasLinks);
            return $hasLinks;

        }catch (\Exception $error){
            //抛出错误
            echo"unable to parse the content";
        }

    }

    /**
     *
     */
    function filter($ele){
        return preg_match('/http:\/\//',$ele);
    }


}
class Book {
    public $name='';
    public $publicDate;
    protected $price;
    function __construct($name,$publicDate,$price){
        $this->name=$name;
        $this->publicDate = $publicDate;
        $this->price=$price;
    }
    function getBookName(){
        return $this->name;
    }
    function setBookName($newName){
        $this->name =$newName;
         }
    function getPice(){
        return $this->price;
         }
    function setPrice($newPrice){
        $this->price=$newPrice;
    }
    function getPublicDate(){
        return $this->publicDate;
    }

}
class Author{
    public $author;
    private $birthday;
    public $hisPublics;

}
