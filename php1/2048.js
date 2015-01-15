/**
 *  2048 游戏为一个简单规则的益智游戏
 *   中午吃饭随便写的， 懒得写前端了。 胜利判断也没写， 就一直玩下去吧。。。
 */
(function(){
var MAX_NUM = 2048,    // 格子可放置最大数字
    GRID_SIZE = 5,     // 格子大小
    BEGIN_POS_NUM = 4, // 开始格子数量
    /// 方向标识
    LEFT_RIGHT = 1,    // 从左到右  
    RIGHT_LEFT = 2,    // 从右道左
    TOP_BOTTOM = 3,    // 从上到下
    BOTTOM_TOP = 4,    // 从下到上
    D_HORI = 0, D_VERT = 1;    // 方向是横向还是竖向
    
/**
 * 获取变量类型
 */
var type = function(v) {
    var class2type = _typeArray = [];
    // 获取类型数组
    _typeArray = "Boolean Number String Function Array Date RegExp Object Error".split(" ");
    for(var i in _typeArray) {
        class2type[ "[object " + _typeArray[ i ] + "]" ] = _typeArray[ i ].toLowerCase(); 
    }
    
    return function(obj) {
       if ( obj == null ) {
            return obj + "";
        }
        return typeof obj === "object" || typeof obj === "function" ?
            class2type[ toString.call(obj) ] || "object" :
            typeof obj;
    };    
}();

/**
 *  判断是否是数组
 */
var isArray = Array.isArray || function(v) {
   return type(v) === "array";
};

/**
 *  对所有格子执行迭代
 */
var each = function(f) {
    var i = 0;
    for(var row = 0; row < GRID_SIZE; row++) {
         for(var col =0; col < GRID_SIZE; col++ ) {
             //console.log(f.arguments[1]);
             var result =  f.call( Game, row, col, i);
             if(result) {
                return result;
             }
             i++;
         }   
    }
};


/**
 *  不同each， 用于不同方向迭代, 以后考虑优化
 */
 // 从右往左迭代
var eachRightLeft = function(f) {
    for(var row = 0 ; row < GRID_SIZE;  row++) {
         for(var col = GRID_SIZE-1; col >= 0; col-- ) {
             var result =  f.call( Game, row, col);
             if(result) {
                return result;
             }
         }
    }
};

// 从左到右迭代
var eachLeftRight = function(f) {
    for(var row = 0 ; row < GRID_SIZE;  row++) {
         for(var col =0; col < GRID_SIZE; col++ ) {
             var result =  f.call( Game, row, col);
             if(result) {
                return result;
             }
         }
    }    
};
// 从顶向下迭代
var eachTopDown = function(f) {
    for(var col = 0 ; col < GRID_SIZE;  col++) {
         for(var row =0; row < GRID_SIZE; row++ ) {
             var result =  f.call( Game, row, col);
             if(result) {
                return result;
             }
         }
    }
};
// 从下向上迭代
var eachDownTop = function(f) {
    for(var col = 0 ; col < GRID_SIZE;  col++) {
        for(var row =GRID_SIZE - 1; row >=0 ; row-- ) {
            var result =  f.call( Game, row, col);
            if(result) {
                return result;
            }
        }
    }
}


/**
 *  游戏对象
 */
var Game = {
    // 放置内容的容器
    container : [ ],
    //目前占用格子数量 
    used     : 0,   
    /**
     *  初始化
     */
    init : function() {
        // 初始化格子， 都为 0
        each(function(row, col){
            if( !isArray( this.container[ row ] ) ) {
                this.container[ row ] = [];
            }
            this.container[ row ][ col ] = 0;
        });
        // 随机放置两个 2 放入格子
        for(var i =0; i < BEGIN_POS_NUM; i++ ) {
           var pos =  this.spamNumber()
           this.setPos( pos[0], pos[1], 2);
        }
        console.log( this.container );       
        
    },
    // 处理行索引
    preIndex: undefined,
    preNum  : null,
    mergeArray : [],
    /**
     * 向指定方向移动
     */
    roll: function(direct) {
        this.preIndex = undefined;
        this.preNum  = null;

        switch(direct) {
            case LEFT_RIGHT:
                 eachLeftRight(function(row, col){
                    this.mergeAndMove(D_HORI, row, col);
                 });
                 eachLeftRight(function(row, col){   
                    this.align(D_HORI, row, col );
                 });
                 break; 
            case RIGHT_LEFT:
                 eachRightLeft(function(row, col){
                    this.mergeAndMove(D_HORI, row, col);
                 });
                 eachRightLeft(function(row, col){
                    this.align(D_HORI, row, col, true );
                 });
                 break;
            case TOP_BOTTOM:
                 eachTopDown(function(row, col){
                     this.mergeAndMove(D_VERT, row, col);       
                 });
                 eachTopDown(function(row, col){ 
                     this.align(D_VERT, row, col );
                 });
                 break;
            case BOTTOM_TOP:
                 eachDownTop(function(row, col){
                     this.mergeAndMove(D_VERT, row, col);   
                 });
                 eachDownTop(function(row, col){
                  this.align(D_VERT, row, col , true);
                 });
                 break;                            
        }
    },
    mergeAndMove: function(dtype, row, col) {
        var i = (dtype == D_HORI) ? row : col;
        if( typeof this.preIndex == 'undefined' ) {
            this.preIndex = i;
        }

        var currNum = this.container[ row ][ col ];
        // 在同一行内，进行处理
        if( this.preIndex == i ) {
            if( isArray(this.preNum) && this.preNum[0] == currNum ) {
                //currNum *= 2;
                this.container[ this.preNum[1] ][ this.preNum[2] ] = currNum * 2;
                this.container[ row ][ col ] = 0; 
            }

        }else{
            // 新的一行      
            this.preIndex = i;
            this.preNum = null;
        }

        if(currNum != 0 ) {
            this.preNum = [currNum, row, col];
        }  
    },
    // 对其操作
    align: function(dtype, row, col, rever) {
        var ri = (dtype == D_HORI) ? col : row;
        var currNum = this.container[ row ][ col ];
        var self = this;
        var swap = function(r) {
            if(dtype == D_HORI) {
                var num = self.container[ row ][ r ];
                if( num != 0 ){
                    self.container[ row ][ col ] = num;
                    self.container[ row ][ r ] = 0;
                    return true;
                   }
            }else{
                var num = self.container[ r ][ col ];
                if( num != 0 ){
                    self.container[ row ][ col ] = num;
                    self.container[ r ][ col ] = 0;
                    return true;
                }
            }
        };
        if( currNum == 0 ) {
            if( rever ) {
               while( ri >= 0) {
                   if(swap(ri)) {
                      break;
                   }
                   ri--;
               }
            }else {
               while( ri < GRID_SIZE -1 ) {
                   ri++;
                   if(swap(ri)) {
                      break;
                   }
               }
            }
        }
    },
    /**
     *  在指定位置放置指定的数字
     */
    setPos: function(row, col) {
        var num = arguments.length == 2 ? 2 : arguments[2];
        this.container[ row ][ col ] = num;
    },
    /**
     *  在空余的格子中产生数字
     */
    spamNumber : function() {
        var remain = Math.pow(GRID_SIZE , 2) - this.used;
        // 如果没有剩余格子了，表示游戏失败
        if( remain == 0 ) {
           return false;
        }
        // 空余格子的偏移量
        var offset = parseInt(Math.random() * remain);
        var pos =  each(function(row, col, i){
           if( this.container[ row ][ col ] == 0 ) {
               if(offset == 0) {
                  return [row, col];
               }
               offset--;
           }
        });
        this.used++;
        return pos;
    }
};

Game.init();
Game.roll(BOTTOM_TOP);
console.log( Game.container );
var pos =  Game.spamNumber();
Game.setPos( pos[0], pos[1], 2);
console.log( Game.container );
Game.roll(LEFT_RIGHT);
console.log( Game.container );
Game.roll(LEFT_RIGHT);
console.log( Game.container );

})();