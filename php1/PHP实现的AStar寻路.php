<?php
/**
 * A星寻路算法，用于游戏中的寻路计算
 */
define('CASTAR_DEBUG_RUN',false);

/**
 *  用于实现RPG游戏中的自动寻路。 这个类支持8向寻路和4向寻路，
 *  目前性能损失主要在 对openlist 列表里最小值进行查找损失， 
 *  下一版本将会使用二叉树进行高速搜索，提升寻路算法性能。
 *  
 *  @author  乐天派 <divein@126.com>
 * 
 */
class CAstar {

    // 最远寻路距离，如果设置为0 则为无设置。
    const MAX_FIND_PATH = 16;
    // 进行4向或者8向寻路
    const FIND_PATH_DIRECTION = 8;
    // S值
    const S_BEVEL = 14;
    const S_FLAT = 10;
    /**
     * @var array 路径的开启列表
     */
    private $openList = array();
    /**
     * @var array 路径的关闭列表
     */
    private $closeList = array();
    
    /**
     * 开始节点，结束节点，当前节点.
     * @var type 
     */
    private $startNode = null;
    private $endNode = null;
    private $currNode = null;
     /**
     * 用来判断是否找不到路了。
     * @var type 
     */
    private $noway = false;
   
    /**
     * @var  游戏地图的障碍数据
     */
    private $mapData ;

    /**
     * 构造函数，设置开始节点，和结束节点，并把当前节点设置为开始节点 
     * 
     */
    public function __construct($startNode, $endNode, &$mapData) {
        $this->startNode = $startNode;
        $this->endNode = $endNode;
        $this->currNode = $startNode;
        $this->mapData  = $mapData;
    }

    
    /****************************************************
      *  类接口，包括设置地图障碍数据， 设置开始节点，设置终点。
      *  最后执行 findPath() 进行寻路，返回路点数组
      *  
      ***************************************************/
    /**
     * 设置地图数据
     * 
     * @param type $mapData 
     */
    public function setMapData(&$mapData) {
        $this->mapData = $mapData;
    }

    /**
     * CAsterNode 设置初始节点
     */
    public function setStartNode() {
        $this->startNode = $node;
    }

    /**
     *  CAsterNode 设置终点节点
     */
    public function setEndNode() {
        $this->endNode = $node;
    }
    

    /**
     * 执行寻路操作.
     */
    public function findPath() {
        $ct = 0;
        while (!$this->doFindPath()) {
            if ($this->noway || $ct >= self::MAX_FIND_PATH) {
                return false;
            }
            $ct++;
        }
        $path = array();
        $node = $this->currNode;
        while ($node !== NULL) {
            $path[] = array($node->x, $node->y);
            $node = $node->parentNode;
        }
        return $path;
    }

    
     
    /********************************************
      * 工具函数
      *
      ********************************************/       
    /**
     * 把节点移动到关闭列表，并从开启列表删除之
     * 
     * @param type $node 
     */
    private function moveToCloseList($node) {
        $this->closeList[$node->x . ',' . $node->y] = 1;
        if ($i = $this->array_search($node->x, $node->y, $this->openList)) {
            array_splice($this->openList, $i);
        }
    }

    /**
     * 获取当前节点到目的节点的G值
     * G值 从起点A，沿着产生的路径，移动到网格上指定方格的移动耗费。
     */
    private function g($dist) {
        if (self::FIND_PATH_DIRECTION == 4) {
            return self::S_FLAT;
        } else {
            if (($dist->x - $this->currNode->x) != 0 && ( $dist->y - $this->currNode->y) != 0) {

                return self::S_BEVEL + $this->currNode->G;
            }
            return self::S_FLAT + $this->currNode->G;
        }
    }

    /**
     * 计算两个节点之间的曼哈顿距离
     * 
     * @param type $node 
     */
    private function h($node) {
        $h = (abs($this->endNode->x - $node->x) + abs($this->endNode->y - $node->y)) * 10;
        //   printf("%d-%d..%d-%d..%d\n",$this->endNode->x,$this->endNode->y,$node->x,$node->y,$h);
        return $h;
    }

    /**
     * 从开启列表中获取node
     * 
     * @param CAstarNode $node 
     */
    private function isOpenList($x, $y) {
        if (($i = $this->array_search($x, $y, $this->openList)) !== false) {
            return $this->openList[$i];
        }
        return false;
    }

    /**
     * 判断节点是否在关闭列表中,如果在，返回关闭列表
     * 
     * @param CAstarNode $node 
     */
    private function isCloseList($x, $y) {
        if (isset($this->closeList[$x . ',' . $y])) {
            return true;
        }
        return false;
    }

    /**
     * array search
     * @param type $node
     * @param type $array 
     */
    private function array_search($x, $y, $array) {
        for ($i = 0; $i < count($array); $i++) {
            if ($x == $array[$i]->x && $y == $array[$i]->y) {
                return $i;
            }
        }
        return false;
    }

    /**
     *  A*中 处理openlistnode 的值增加
     *  1.第一步，处理当前步并获取开放列表 
     * 
     * @param array $data  一个实现了 IMapData接口的地图数据对象
     */
    private function doFindPath() {
        $tmpNode = null;

        for ($x = max($this->currNode->x - 1, 0); $x <= min($this->currNode->x + 1, 100); $x++) {
            for ($y = max($this->currNode->y - 1, 0); $y <= min($this->currNode->y + 1, 100); $y++) {
                if (self::FIND_PATH_DIRECTION == 4) {
                    if (($this->currNode->x - $x ) != 0 && ($this->currNode->y - $y) != 0) {
                        continue;
                    }
                }
                if ($x == $this->currNode->x && $y == $this->currNode->y)
                    continue;
                // 排除关闭列表，和地图上障碍物
                // 然后把剩下的放到开放列表中
                if (!$this->isCloseList($x, $y) && empty($this->mapData[$x.','.$y])) {
                    //1. 如果已经在开放列表中了，则比较当前到位置的G值,找到最小G值的,并把当前设置为G值的父对象.
                    if ($openNode = $this->isOpenList($x, $y)) {
                        if ($openNode->getF() < $this->currNode->getF()) {
                            if (empty($tmpNode)) {
                                $tmpNode = $openNode;
                            } else {
                                if ($openNode->getF() < $tmpNode->getF()) {
                                    $tmpNode = $openNode;
                                }
                            }
                        }
                    } else {
                        // 建立新的Node.并放入开放列表中去。
                        $openNode = new CAstarNode($x, $y, $this->currNode);
                        $openNode->H = $this->h($openNode);
                        $openNode->G = $this->g($openNode);
                        $this->openList[] = $openNode;
                    }

                    if ($openNode->x == $this->endNode->x && $openNode->y == $this->endNode->y) {
                        $this->currNode = $openNode;
                        return true;
                    }
                }
            }
        }
        if (!empty($tmpNode)) {
            $this->moveToCloseList($this->currNode);
            $this->currNode = $tmpNode->parentNode;
        }

        if ($this->processOpenList() === false) {
            $this->noway = 1;
            return true;
        }
        return false;
    }

    /**
     * 找出开放列表中F值最小的数
     */
    private function findMinF() {
        $minF;
        $minFIndex = 0;
        if ($count = count($this->openList)) {
            if ($count == 1)
                return $this->openList[0];
            else {
                $minF = $this->openList[0]->getF();
                for ($i = 1; $i < $count; $i++) {
                    $value = $this->openList[$i]->getF();

                    if ($value < $minF) {
                        $minF = $value;
                        $minFIndex = $i;
                    }
                }
            }

            return $this->openList[$minFIndex];
        } else {
            return false;
        }
    }

    /**
     * 处理开放列表
     */
    private function processOpenList() {
        if (($i = $this->findMinF()) === false) {
            return false;
        } else {

            $this->moveToCloseList($this->currNode);
            $this->currNode = $i;
            return true;
        }
    }

}

/**
 * A星寻路的节点类 
 */
class CAstarNode {

    /**
     * 节点的G值。。 一般水平移动是10， 斜向移动是14
     * 对于四项寻路，为常量10.节点G值会加上父节点的G值
     * @var integer
     */
    public $G = 0;
    /**
     * 节点的曼哈顿距离。
     * @var integer
     */
    public $H = 0;
    
    /**
     * 节点的父节点
     * @var integer
     */
    public $parentNode;
    public $x;
    public $y;

    /**
     * 构造函数
     * 
     * @param $astar astar对象 
     * @param $x     x坐标
     * @param $y     y坐标
     */
    public function __construct($x, $y, $parentNode=null) {
        $this->parentNode = $parentNode;
        $this->x = $x;
        $this->y = $y;
    }

    /* *
     * 获取F值。 
     */
    public function getF() {
        return $this->G + $this->H;
    }
}

// 测试
if (CASTAR_DEBUG_RUN) {
    //地图开始位置和结束位置
    $startNode = new CAstarNode(2, 2);
    $endNode = new CAstarNode(6, 6, null);
    //障碍物
    $mapData = array('4,4' => 1, '2,4' => 1,'3,6'=>1,'4,6'=>1);
    $astar = new CAstar($startNode, $endNode,$mapData);
    $path = $astar->findPath();
    
    var_dump($path);
}