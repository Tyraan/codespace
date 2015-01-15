<?php
/**
 * 解决8皇后问题
 * 8皇后为一个经典的计算机科学谜题： 有一个棋盘和8个要放到上面的皇后,
 * 唯一要求是皇后之间不能形成威胁。也就是说，必须把它们放置成每个皇后都不能吃掉其他皇后的状态。
 *
 * 写程序在于思考，欢迎一起讨论算法。哈哈, 执行本程序请改名为英文(eg.queen.php) 然后:
 *
 *  php -f  queen.php
 *
 * @author wangxinyi<divein@126.com>
 * @create_time 2013-05-30
 */

$states = array();
/**
 *  冲突检测
 *  nextX 表示下一个皇后坐标的水平位置， nextY 表示垂直位置（y坐标或行).
 *  这个坐标对前面每个皇后位置做一个简单的检查， 如果下一个皇后和前面的皇后有同样的水平位置，
 *  或者是在一条对角线上，就会发生冲突，接着返回True. 如果没有冲突，那么返回False
 *
 *  @param  $state array 表示棋盘， 
 *  @param  $nextX integer 表示下一个皇后的水平位置，(x坐标或列)
 */
function conflict($state, $nextX) {
    $nextY = count($state);
    // 检查之前列和当前列的冲突
    for( $i=0; $i < $nextY; $i++ ) {
        $pos = abs($state[$i] - $nextX);
        if($pos == 0 || $pos == $nextY-$i) {
            return true;
        }
    }
    return false;
}

/**
 *  处理8皇后
 *
 *  @param  $num  integer  皇后数量
 *  @param  $state array 棋盘
 */
function queen($num, $state = array()) {
    global $states;
    for($pos = 0; $pos < $num; $pos++){
        if(!conflict($state, $pos)) {
            $arr  = array_merge($state , array($pos));
            if(count($arr) == $num){
                $states[] = $arr;
                return ; 
            }else{
                queen($num, $arr); 
            }
        }
    }
}

/**
 *  打印最后显示结果
 *
 *  @param $state array 棋盘数据
 */
function printState($state) {
    $size = count($state);
    $line =  str_repeat('+-', $size)."+\n";
    for($i =0; $i < $size; $i++){
        echo $line; 
        for($j=0; $j < $size; $j++){
            if($state[$i]==$j) {
                echo '|Q'; 
            }else{
                echo '| ';
            } 
            if($j == $size-1) echo "|\n"; 
        }
    }
    echo $line."\n";
}

/**
 * 执行
 *
 * @param $queen integer 皇后数量
 * @param $size  integer 输出多少种
 */
function run($queen,$size) {
    global $states;
    queen($queen); 

    $count =count($states);
    echo "---------------------------------------\n";
    echo "  grid: $queen, passible: $count      \n";
    echo "---------------------------------------\n";

    shuffle($states);  
    for($i =0; $i<$size; $i++){
        $arr = array_pop($states);
        printState($arr);
    }
}

run(8,3);
