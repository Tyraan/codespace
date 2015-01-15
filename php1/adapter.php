<?php
/**
 * Created by PhpStorm.
 * User: Tyraan
 * Date: 2015/1/12
 * Time: 11:11
 */

class Target{
    public function hello(){
        echo 'Hello';
    }
    public function world(){
        echo 'world';
    }

}
class Client{
    public static function main(){
        $Target = new Target();
        $Target->hello();
        $Target->world();
    }
}
Client::main();

interface Target{
    public function hello();
    public function world();

}
class Adaptee
{
    public function world()
    {
        echo ' world <br />';
    }

    /**
     * 加入新的方法
     */
    public function greet()
    {
        echo ' Greet ';
    }
}
class Adapter extends Adaptee implements Target{
    public function hello(){
        parent::greet();
    }

}

