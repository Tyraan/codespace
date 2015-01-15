<?php
/**
 * Created by PhpStorm.
 * User: Tyraan
 * Date: 2014/12/19
 * Time: 10:55
 */
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
class BookC extends Book {
    public function __clone(){
        $this->name = parent::$name;
        $this->publicDate=parent::$publicDate;
        $this->price= parent::$price;
        }
    }

$testOr=new Book('Learning Php','February 2013',40);
$testNoneRewriteCloneMethod=clone $testOr;
$testNoneRewriteCloneMethod->setBookName('Programming Php,third edition');
echo 'this none define clone method object'.'</br>';
echo $testOr->getBookName().'</br>';
print $testNoneRewriteCloneMethod->getBookName().'</br>';
?>
<?php
trait Drive {
    public $carName = 'trait';
    public function driving() {
        echo "driving {$this->carName}\n";
    }
}
class Person {
    public function eat() {
        echo "eat\n";
    }
}
class Student extends Person {
    use Drive;
    public function study() {
        echo "study\n";
    }
}
$student = new Student();
echo'<br/>';
$student->study();
echo'<br/>';
$student->eat();
echo'<br/>';
$student->driving();echo'<br/>';


