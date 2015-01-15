<html>
<body>
<?php
             class TestConst {
                 const COUNTRY = 'China';
                 static $static = 'Static';    
                 
                 public function getCountry() {
                     return self::COUNTRY;
                 }
             }
             $test = new TestConst();
             var_dump($test);
             echo '<br>';
echo $test->getCountry() . '<br>';
echo TestConst::COUNTRY . '<br>';

?>
<?php
             const COUNTRY = 'Japan';
             echo COUNTRY . '<br>';
?>
</body>
</html>