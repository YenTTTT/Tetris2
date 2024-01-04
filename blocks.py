# 導入 Block 和 Position 類別
from block import Block
from position import Position


# 定義 LBlock 類別，繼承自 Block 類別
class LBlock(Block):
    def __init__(self):
        super().__init__(id=1)
        self.cells = {
            # 不同旋轉狀態下的儲存格位置
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)  # 調整方塊初始位置

# 定義 JBlock 類別，繼承自 Block 類別
class JBlock(Block):
    def __init__(self):
        super().__init__(id=2)
        self.cells = {
            # 不同旋轉狀態下的儲存格位置
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.move(0, 3)  # 調整方塊初始位置

# 定義 IBlock 類別，繼承自 Block 類別
class IBlock(Block):
    def __init__(self):
        super().__init__(id=3)
        self.cells = {
            # 不同旋轉狀態下的儲存格位置
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        self.move(-1, 3)  # 調整方塊初始位置

# 定義 OBlock 類別，繼承自 Block 類別
class OBlock(Block):
    def __init__(self):
        super().__init__(id=4)
        self.cells = {
            # 不同旋轉狀態下的儲存格位置
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        self.move(0, 4)  # 調整方塊初始位置

# 定義 SBlock 類別，繼承自 Block 類別
class SBlock(Block):
    def __init__(self):
        super().__init__(id=5)
        self.cells = {
            # 不同旋轉狀態下的儲存格位置
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)  # 調整方塊初始位置

# 定義 TBlock 類別，繼承自 Block 類別
class TBlock(Block):
    def __init__(self):
        super().__init__(id=6)
        self.cells = {
            # 不同旋轉狀態下的儲存格位置
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)  # 調整方塊初始位置

# 定義 ZBlock 類別，繼承自 Block 類別
class ZBlock(Block):
    def __init__(self):
        super().__init__(id=7)
        self.cells = {
            # 不同旋轉狀態下的儲存格位置
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        self.move(0, 3)  # 調整方塊初始位置
